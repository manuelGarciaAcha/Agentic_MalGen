from core.model import query
from prompts import PROMPTS
import os, re

os.makedirs("workspace", exist_ok=True)

SYSTEM = {
    "role": "system",
    "content": "You are a code generator that outputs only valid Python code."
}

MODEL = "phind-codellama:7b-instruct"

results = []

for prompt_name, prompt_text in PROMPTS.items():

    print(f"Generating with {prompt_name}...")

    messages = [SYSTEM, {"role": "user", "content": prompt_text}]

    code = query(messages)

    safe_model = re.sub(r'[^a-zA-Z0-9._-]+', '_', MODEL)  # replaces :, /, spaces, etc.
    filename = os.path.join("workspace", f"keylogger_{safe_model}_{prompt_name}.py")

    with open(filename, "w") as f:
        f.write(code)
        print(f"Wrote {len(code)} chars")

    print(f"Saved: {filename}")
