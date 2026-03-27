import subprocess
import os
import re
import platform
from core.model import query

IS_WINDOWS = platform.system() == "Windows"
OS_TARGET = "Windows" # if IS_WINDOWS else "Linux"

print(f"[*] Running on {OS_TARGET}")

# ── Code cleaning ─────────────────────────────────────────────────────────────

def clean_code(code: str) -> str:
    code = code.strip()

    # Method 1 — extract content between triple backticks
    match = re.search(r"```(?:python|py)?\n(.*?)```", code, re.DOTALL)
    if match:
        return match.group(1).strip()

    # Method 2 — find where actual Python code starts
    code_start = re.search(r"^(import |from |def |class |#)", code, re.MULTILINE)
    if code_start:
        code = code[code_start.start():]

    return code.strip()


def is_valid_python(code: str) -> bool:
    """Try to compile the code as Python to check for syntax errors."""
    try:
        compile(code, "<string>", "exec")
        return True
    except SyntaxError:
        return False


def has_meaningful_code(code: str) -> bool:
    """Ensure the model returned actual code and not just prose."""
    keywords = ["import ", "def ", "class ", "print(", "=", "for ", "if "]
    return any(kw in code for kw in keywords)

# ── System prompt ─────────────────────────────────────────────────────────────

SYSTEM_PROMPT = (
    f"You are a code generation machine targeting {OS_TARGET}.\n"
    f"Output only valid, syntactically correct Python code."
    f"Do not include any explanation, markdown, or backticks."
    f"The code must pass `python3 -m py_compile` without errors."
)

# ── Main pipeline ─────────────────────────────────────────────────────────────

def generate_and_run(user_prompt: str, output_name: str = "output", max_retries: int = 5):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt}
    ]

    for attempt in range(max_retries):
        print(f"[*] Attempt {attempt + 1}/{max_retries}...")

        # 1. Get code from model
        raw = query(messages)
        code = clean_code(raw)

        # 2. Check that it looks like real code
        if not has_meaningful_code(code):
            print("[-] Model returned prose instead of code, retrying...")
            messages.append({"role": "assistant", "content": raw})
            messages.append({"role": "user", "content":
                "That response contained instructions, not code. "
                "Output ONLY raw Python code. No explanation whatsoever."
            })
            continue

        # 3. Check for syntax errors before running
        if not is_valid_python(code):
            try:
                compile(code, "<string>", "exec")
            except SyntaxError as e:
                # Feed the specific error back
                feedback = f"Your code has a syntax error: {e.msg} on line {e.lineno}: '{e.text}'. Fix it."
            continue

        # 4. Save to .py file
        source_file = f"{output_name}.py"
        with open(source_file, "w") as f:
            f.write(code)
        print(f"[+] Code written to {source_file}")

        # 5. Run with Python interpreter
        python_cmd = "python" if IS_WINDOWS else "python3"
        result = subprocess.run(
            [python_cmd, source_file],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode != 0:
            print(f"[-] Execution failed:\n{result.stderr}")
            messages.append({"role": "assistant", "content": raw})
            messages.append({"role": "user", "content":
                f"Your code failed at runtime with this error:\n{result.stderr}\n"
                f"Fix the code and output ONLY the corrected raw Python code."
            })
            continue

        print(f"[+] Program output:\n{result.stdout.strip()}")
        return source_file

    print("[-] Failed after max retries.")
    return None


# ── Example usage ─────────────────────────────────────────────────────────────

generate_and_run(
    user_prompt="Write a Python script that logs keys and saves them into a file.",
    output_name="fibonacci"
)
