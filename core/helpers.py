import json
import re
from typing import Dict


def extract_json_object(raw: str) -> dict:
    raw = raw.strip()

    raw = "\n".join(
        line.lstrip("> ").rstrip()
        for line in raw.splitlines()
    ).strip()

    raw = re.sub(r"^```(?:json)?\s*", "", raw, flags=re.IGNORECASE)
    raw = re.sub(r"\s*```$", "", raw)

    start = raw.find("{")
    end = raw.rfind("}")

    if start == -1 or end == -1 or end <= start:
        raise ValueError("No JSON object found")

    candidate = raw[start:end + 1]

    candidate = (
        candidate
        .replace("“", '"')
        .replace("”", '"')
        .replace("‘", "'")
        .replace("’", "'")
    )

    candidate = re.sub(r",\s*([}\]])", r"\1", candidate)

    return json.loads(candidate)