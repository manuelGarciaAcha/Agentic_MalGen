import sys
sys.path.append('../')

from core.comms import *
import json
from core.model import query
from typing import List, Dict, Any



class Generator:
    def __init__(self):
        pass

    def build_prompt(
        self,
        goal: str,
        past_code: str,
        fix_items: List[FixItem],
        iteration: int,

    )-> List[Dict[str,str]]:
        if fix_items:
            fix_block = "\n".join(
                f"- [{f.severity}] {f.id}: {f.instruction}"
                for f in fix_items
            )
        else:
            fix_block = "- None"

        system = (
            "You are a pure code generator that is tasked with generating JSON files.\n\n"

	    "Definitions:\n"
	    '- "Response" = The entire text you return.\n'
	    '- "Output" = The value inside the "code" field of the JSON object.\n'
	    '- "JSON Object" = A singular, valid JSON object.\n\n'


        "Format Constraints:\n"
	    "- Response must begin with '{' and end with '}'.\n"
	    "- Response must be exactly one JSON object"
	    "- No markdown, no code fences, no explanations, no extra text.\n"
	    '- The JSON Object keys must be exactly: "code", "applied_fixes", "notes".\n'
            '- "code" must be a string containing Output.\n'
	    '- "applied_fixes" must be an array of strings.\n'
	    '- "notes" must be a string.\n'
	    '- No text outside of the JSON object.\n'
	    '- Do NOT wrap the JSON object in backticks\n\n'
        
        'Implementation Constraints:\n'
        'On First Iteration: generate code that satisfies the goal as closely as possible.\n'
        'On Iteration 2 and Higher: utilizing the past code as a base, implement the required fixes onto that code, while maintaining the goal specified in mind.\n'
        '- Once past the first iteration, resolving fixes is of the highest priority.\n'
        '- Resolve all fix requests unless already satisfied in code.\n'
        '- List the IDs of the fixes you addressed in the "applied_fixes" field.\n'
        '- Only include a fix ID in "applied_fixes" if the returned code completely resolves it.\n'
        '- Ensure to maintain existing behavior that is unreferenced or properly functioning.\n'
        f'- For the case of an issue which states {RETRY_FIRST_ITERATION}, treat the implementation as if it were the first iteration.\n'
        f'- For the case of an issue which states {REVIEWER_FORMAT_ERR} or {REVIEWER_JSON_ERR}, resend the last attempt without any edits.\n\n'


	    "If you cannot comply exactly with the above contract, output exactly:\n"
	    '{"code":"","applied_fixes":[],"notes":"ERROR: Generator Format Error"}\n\n'

	    "Example:\n"
	    '{"code":"print(\\"hello\\")","applied_fixes":["iteration1_issue1"],"notes":"updated X"}'
	)
        user = (


            f"Goal:\n{goal}\n\n"
            f"----- BEGIN CODE -----\n\n {past_code}\n ----- END CODE -----\n\n"
            f"Required Fixes:\n {fix_block}\n\n"
            f"Iteration: {iteration}\n"

        )
        return [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ]


    def generate(
        self,
        goal: str,
        past_code: str,
        fix_items: List[FixItem],
        iteration: int,
    )-> Draft:

        fix_items = fix_items or []
        prompt = self.build_prompt(goal, past_code, fix_items, iteration)
        raw = query(prompt)

        print(raw)

        data = self._parse_json_generator(raw)

        return Draft(
            output = data.get("code", ""),
            applied_fixes = list(data.get("applied_fixes", [])),
            notes = str(data.get("notes", "")),
            iterations=iteration,
        )
    def _parse_json_generator(self, raw: str) -> dict:
        try:
            raw = raw.strip()
            if raw.startswith("```"):
                raw = raw.strip("`")
                raw = raw.replace("json", "", 1).strip()

            if raw.startswith(">"):
                raw = raw.lstrip("> ").strip()

            return json.loads(raw)
        except Exception as e:
            print("Generator JSON Parse failed", e)

            return {
                "code":"",
                "applied_fixes":[],
                "notes": {GENERATOR_JSON_ERR}
                }
