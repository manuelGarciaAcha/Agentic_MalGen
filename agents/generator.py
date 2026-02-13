import sys
sys.path.append('../')

from core.comms import Draft, ReviewResult, FixItem
import json
from core.model import query
from typing import List, Dict, Any



class Generator:
    def __init__(self):
        
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
                "You are a code generator. \n"
                "Return only valid JSON with these exact keys:\n"
                '- "code": string(fully updated code)\n'
                '- "applied_fixes": array of fix IDs that have been addressed\n'
                '- "notes": a short descriptor of changes\n'

                "No markdown. No commentary. JSON ONLY. \n"
            )
            user = (
            
                "Produce an updated version of the code that satisfies the goal. \n\n"
                
                f"Goal:\n{goal}\n\n"
                
                "Code (Edit this; keep unrelated parts stable):\n"
                "BEGIN CODE\n"
                f"{past_code}\n"
                "END CODE\n\n"

                "Fixes to apply (Prioritize blocking issues first):\n"
                f"{fix_block}\n\n"

                "Output Format (CRITICAL):\n"
                "Return only valid JSON with these exact keys:\n"
                '- "code": string(fully updated code)\n'
                '- "applied_fixes": array of fix IDs that have been addressed\n'
                '- "notes": a short descriptor of changes\n'

                "No markdown. No commentary. JSON ONLY. \n"
                f"Iteration: {iteration}"

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

            data = self._parse_json_strict(raw)

            return Draft(
                code = data["code"],
                applied_fixes = list(data.get("applied_fixes", [])),
                notes = str(data.get("notes", "")),
                iteration=iteration,
            )
        def _parse_json_strict(self, raw: str) -> dict:
            raw = raw.strip()
            if raw.startswith("```"):
                raw = raw.strip("`")
                raw = raw.replace("json", "", 1).strip()

            return json.loads(raw)













