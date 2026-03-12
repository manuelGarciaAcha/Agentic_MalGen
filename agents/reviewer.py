import sys
sys.path.append('../')

from core.comms import *
import json
from core.model import query
from typing import List, Dict, Any, Literal


class Reviewer:
    def __init__(self):
        pass

    # Prompt construction for LLM consumption
    def build_prompt(
        self,
        goal: str, # general agentic goal
        code: str,
        fix_items: List[FixItem],
        metrics: Dict[str, str], # goal specific rubric criteria
        iteration: int,

    )-> List[Dict[str,str]]:
        if fix_items:
            fix_block = "\n".join(
                f"- [{f.severity}] {f.id}: {f.instruction}"
                for f in fix_items
            )
        else:
            fix_block = "- None"

        metrics_keys = ", ".join(f'"{k}"' for k in metrics.keys())
        metrics_descriptions = "\n".join(
            f'- "{k}": "{v}"'
            for k,v in metrics.items()
        )

        # zero out keys for failure case
        fallback_metrics = {k: 0 for k in metrics.keys()}
                
        system = (
            "You are a dedicated and meticulous code reviewer. All responses you provide are to be in the following format.\n\n"

	    "Definitions:\n"
	    '- "Response" = The entire text you return.\n'
	    '- "JSON Object" = A singular, valid JSON object.\n\n'


            "Constraints:\n"
	    "- Response must begin with '{' and end with '}'.\n"
	    "- Response must be exactly one JSON object.\n"
	    "- No markdown, no code fences, no explanations, no extra text.\n"
	    '- The JSON Object keys must be exactly: "overall_score", "subscores", "issues", "summary".\n'
            '- "overall_score" must be an average taken from the "subscores" field expressed as an integer (rounding to the nearest integer). \n'
	    f'- "subscores" must be a dictionary of these exact keys {metrics_keys} and their integer values between 0 and 10.\n'
        '- a "subscores" entry with a value lower than 7 must have a justification in "issues"\n'
	    '- "issues" must be an array of strings. Each issue must describe a concrete problem and include brief evidence such as a function name, line reference, or code fragment. \n'
        '- "summary" must be a string.\n'
	    '- No text outside of the JSON object.\n'
        '- Do not report the same issue multiple times in different wording.\n'
	    '- Do NOT wrap the JSON object in backticks\n'
        '- Do not report incorrect issues that are not explicitly supported by the code.\n'
        '- Do not split one syntax problem into multiple redundant issues.\n'
        f'- Should the code for review be empty or blank, include the issue {RETRY_FIRST_ITERATION}.\n'
        '- Review the code against every explicit requirement in the goal. Missing any stated requirement must be reported as an issue.\n\n'

        'Metric Definitions:\n'
        f'{metrics_descriptions}\n\n'

	    "If you cannot comply exactly with the above contract, output exactly:\n"
	    f'{{"overall_score":0,"subscores":{{{fallback_metrics}}},"issues":[{REVIEWER_FORMAT_ERR}],"summary": "FORMAT_ERROR"}}\n\n'
	    "Example:\n"
	    '{"overall_score":5,"subscores":{"code_correctness": 5, "goal_alignment": 4, "readability": 6},"issues":["Syntax error in line 2"],"summary": "Fails to align with goal, decent code generation, 1 issue"}\n\n'
	)
        user = (
        
            f"Goal:\n{goal}\n\n"
            f"Code:\n ----- BEGIN CODE -----\n {code} \n ----- END CODE -----\n\n"
            f"Previous Fix Requests (may already be addressed):\n {fix_block}\n\n"
            f"Iteration:\n {iteration}\n\n"

        )
        return [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ]

    # Output generation and standardization: contains the review in strict JSON
    def review(
        self,
        goal: str,
        past_code: str,
        fix_items: List[FixItem],
        metrics: Dict[str,str],
        iteration: int,
    )-> ReviewResult:

        fix_items = fix_items or []
        prompt = self.build_prompt(goal, past_code, fix_items, metrics, iteration)
        raw = query(prompt)

        print(raw)

        data = self._parse_json_reviewer(raw, metrics)
        subscores = data.get("subscores",{})
        overall_score = round(sum(subscores.values()) / len(subscores)) if subscores else 0
        print(f"OVERALL: {overall_score}\n\n\n")

        return ReviewResult(
            overall_score = overall_score,
            subscores = subscores,
            issues = list(data.get("issues", [])),
            summary = str(data.get("summary", ""))
        )

    # Basic LLM output clean-up for proper JSON result
    def _parse_json_reviewer(self, raw: str, metrics: Dict[str,str]) -> dict:
        try:
            raw = raw.strip()
            if raw.startswith("```"):
                raw = raw.strip("`")
                raw = raw.replace("json", "", 1).strip()

            if raw.startswith(">"):
                raw = raw.lstrip("> ").strip()

            return json.loads(raw)
        except Exception as e:
            print(f"Reviewer JSON Parse failed", e)

            # zero out keys for failure case
            fallback_metrics = {k: 0 for k in metrics.keys()} 

            return {
                "overall_score":0,
                f"subscores": fallback_metrics,
                f"issues":[REVIEWER_JSON_ERR],
                "summary": "JSON ERROR"
            }   