import os
import json
import ast
import sys
import re
from dataclasses import dataclass, asdict
from typing import List, Dict

from agents.generator import Generator
from agents.reviewer import Reviewer
from core.comms import FixItem, Draft, ReviewResult
from core.prompts import PROMPTS

@dataclass
class Runner:
    generator: Generator
    reviewer: Reviewer

    def write_json_logs(self, path:str, data:dict) -> None:
        with open(path, "w", encoding= "utf-8") as f:
            json.dump(data, f, indent=2)

    def conv_issues_to_fixitems(self, issues: List[str], iteration: int) -> List[FixItem]:
        fix_items = []
        for i, issue in enumerate(issues, start=1):
            fix_items.append(
                FixItem(
                    id=f"iteration{iteration}_issue{i}",
                    title=f"Reviewer Issue {i}",
                    instruction=issue,
                    severity="major",
                    status="open",
                )
            )
        return fix_items

    def struct_python_src_code(self, code : str) -> str:
        if not code or not code.strip():
            return False, "", "empty or whitespace"
        corrected = code.replace("\r\n", "\n").strip() + "\n"

        try: 
            ast.parse(corrected)
            return True, corrected, ""
        except SyntaxError as e:
            return False, corrected, f"{e.msg} at line {e.lineno}, offset {e.offset}"


    def write_python_file(
        self,
        source: str,
        out_dir: str,   
    )-> str:


        dir_name = os.path.basename(os.path.dirname(os.path.normpath(out_dir)))
        file_name = f"{dir_name}_output.py"
        file_path = os.path.join(out_dir, file_name)
        with open(file_path, "w", encoding= "utf-8") as f:
            f.write(source)

        return file_path

    def run(
        self,
        goal: str,
        metrics: Dict[str,str],
        test_dir_name: str,
        min_iterations: int = 1,
        max_iterations: int = 10,
        log_dir: str = "./workspace",
    ) -> dict:
        if min_iterations < 1:
            raise ValueError("minimum iterations must be at least one")

        if max_iterations < min_iterations:
            raise ValueError("maximum iterations must be greater than minimum iterations")

        fix_items: List[FixItem] = []
        curr_code = ""
        stop_reason = "max_iterations_reached"
        final_gen = None
        final_review = None
        final_score = 0
        final_issue_cnt = 0

        test_dir = os.path.join(log_dir, test_dir_name)
        os.makedirs(test_dir, exist_ok = True)

        for i in range(1, max_iterations +1):
            cont_loop = True

            i_dir = os.path.join(test_dir, f"iteration_{i}")
            os.makedirs(i_dir, exist_ok=True)

            draft: Draft = self.generator.generate(
                goal=goal,
                past_code = curr_code,
                fix_items = fix_items,
                iteration = i,
            )

            if not draft.output or not draft.output.strip():
                review = ReviewResult(
                    overall_score=0,
                    subscores={k: 0 for k in metrics},
                    issues=["Generator produced empty or whitespace-only code. Retry generation from the previous valid code."],
                    summary=f"Generator failed or produced empty output: {draft.notes}",
                )

                print("DEBUG review type:", type(review))
                print("DEBUG review value:", review)

                self.write_json_logs(
                    os.path.join(i_dir, f"generator_output_{i}.json"),
                    asdict(draft),
                )
    
                self.write_json_logs(
                    os.path.join(i_dir, f"reviewer_output_{i}.json"),
                    asdict(review),
                )

                final_gen = draft
                final_review = review

                fix_items = self.conv_issues_to_fixitems(review.issues, i)
                continue
            
            curr_code = draft.output

            review: ReviewResult = self.reviewer.review(
                goal=goal,
                past_code = curr_code,
                fix_items = fix_items,
                metrics = metrics,
                iteration = i,
            )
        
            print("DEBUG review type:", type(review))
            print("DEBUG review value:", review)

            self.write_json_logs(
                os.path.join(i_dir, f"generator_output_{i}.json"),
                asdict(draft),
            )

            self.write_json_logs(
                os.path.join(i_dir, f"reviewer_output_{i}.json"),
                asdict(review),
            )

            pass_score = 7
            
            # Enforce a passing score of 7 or higher
            low_scores = [
                (name, score)
                for name, score in review.subscores.items()
                if score < pass_score
            ]

            if low_scores and not review.issues:
                review.issues.append("One or more subscores are below 7 without justification")

            if i >= min_iterations and review.overall_score >= pass_score and len(review.issues) == 0 and isinstance(review.issues, list):
                cont_loop = False
                stop_reason = "No Issues, Passing Score"

            final_gen = draft
            final_review = review

            if not cont_loop:
                break

            fix_items = self.conv_issues_to_fixitems(review.issues, i)

        if final_review:
            final_score = final_review.overall_score
            final_issue_cnt = len(final_review.issues)
        else:
            final_score = 0
            final_issue_cnt = 0

        summary = {
            "goal": goal,
            "metrics": metrics,
            "completed_iterations": i,
            "stop_reason": stop_reason,
            "final_score": final_score,
            "final_issue_count": final_issue_cnt,
            "code": final_gen.output if final_gen else "",
        } 

        self.write_json_logs(
                os.path.join(i_dir, f"final_output.json"),
                summary,
            )
        
        ok, source, py_error = self.struct_python_src_code(final_gen.output) if final_gen else ""
        
        if ok:
            self.write_python_file(
                source = source,
                out_dir = i_dir,
            )


        print(f"{summary}")

        return {
            "summary": summary,
        }

def sanitize_model_name(name: str) -> str:
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name)

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: = python3 runner.py <prompt_num> <model_name>")
        exit(1)

    # Prompt choice is implemented in CLI.
    prompt_choice = int(sys.argv[1])
    goal = PROMPTS[prompt_choice] if prompt_choice in PROMPTS else None

    model = sys.argv[2]

    dir_model_name = sanitize_model_name(model)

    if goal is None:
        print("Invalid prompt number")
        exit(1) 
    
    # Reviewer 'grading' criteria
    metrics = {
        "code_correctness": "Does the code function correctly? Full marks requires: 0 syntax errors, proper code structure and no runtime or compiliation errors.",
        "alignment_to_goal": "Does the code solve the goal? Full marks requires for every requirement of the goal to be fulfilled.",
        "readibility": "Is the code clean and understandable? Full marks requires proper code structure and naming conventions."
    }

    runner = Runner(generator=Generator(model), reviewer=Reviewer(model))

    # Execution
    runner.run(goal=goal, metrics=metrics, test_dir_name = f"{dir_model_name}_PROMPT{prompt_choice}")
