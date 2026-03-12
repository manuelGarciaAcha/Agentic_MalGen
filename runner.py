import os
import json
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Literal

from agents.generator import Generator
from agents.reviewer import Reviewer
from core.comms import FixItem, Draft, ReviewResult

@dataclass
class Runner:
    generator: Generator
    reviewer: Reviewer

    def _write_json_logs(self, path:str, data:dict) -> None:
        with open(path, "w", encoding= "utf-8") as f:
            json.dump(data, f, indent=2)

    def _conv_issues_to_fixitems(self, issues: List[str], iteration: int) -> List[FixItem]:
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

            i_dir = os.path.join(test_dir, f"iteration_{i}")
            os.makedirs(i_dir, exist_ok=True)

            draft: Draft = self.generator.generate(
                goal=goal,
                past_code = curr_code,
                fix_items = fix_items,
                iteration = i,
            )

            curr_code = draft.output

            review: ReviewResult = self.reviewer.review(
                goal=goal,
                past_code = curr_code,
                fix_items = fix_items,
                metrics = metrics,
                iteration = i,
            )
        
            self._write_json_logs(
                os.path.join(i_dir, f"generator_output_{i}.json"),
                asdict(draft),
            )

            self._write_json_logs(
                os.path.join(i_dir, f"reviewer_output_{i}.json"),
                asdict(review),
            )

            cont_loop = True

            if i >= min_iterations and len(review.issues) == 0:
                cont_loop = False
                stop_reason = "No Issues"

            final_gen = draft
            final_review = review

            if not cont_loop:
                break

            fix_items = self._conv_issues_to_fixitems(review.issues, i)

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

        self._write_json_logs(
                os.path.join(i_dir, f"final_output.json"),
                summary,
            )

        print(f"{summary}")

        return {
            "summary": summary,
        }

if __name__ == "__main__":

    # prompt here
    goal = """
        Write a Python program that loads student grade data from a CSV-style string.
        Each line has: name,score
        The program should:
        1. Ignore empty lines
        2. Skip malformed rows
        3. Convert scores to integers
        4. Return a dictionary with:
            - "average"
            - "highest"
            - "lowest"
            - "passed_students" (score >= 60)
        If there are no valid students, return average=0, highest=None, lowest=None, passed_students=[].
    """
    
    # reviewer 'grading' criteria
    metrics = {
        "code_correctness": "Does the code function correctly? Full marks requires: 0 syntax errors, proper code structure and no runtime or compiliation errors.",
        "alignment_to_goal": "Does the code solve the goal? Full marks requires for every requirement of the goal to be fulfilled.",
        "readibility": "Is the code clean and understandable? Full marks requires proper code structure and naming conventions."
    }

    runner = Runner(generator=Generator(), reviewer=Reviewer())

    # workspace directory
    runner.run(goal=goal, metrics=metrics, test_dir_name = "2_agent_test_basic_code_gen_3")