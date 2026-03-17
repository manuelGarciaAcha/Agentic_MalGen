import subprocess
import os
import re
import platform
from core.model import query

# Detect OS once at startup
IS_WINDOWS = platform.system() == "Windows"
OS_TARGET = "Windows" if IS_WINDOWS else "Linux"

print(f"[*] Running on {OS_TARGET}")

# Headers that are valid on each OS
ALLOWED_HEADERS = {
    "Windows": [
        "stdio.h", "stdlib.h", "string.h", "math.h", "time.h",
        "windows.h", "conio.h", "winsock2.h", "winbase.h"
    ],
    "Linux": [
        "stdio.h", "stdlib.h", "string.h", "math.h", "time.h",
        "unistd.h", "fcntl.h", "sys/types.h", "sys/stat.h",
        "sys/wait.h", "sys/socket.h", "errno.h", "signal.h",
        "pthread.h", "dirent.h", "limits.h", "stdint.h", "stdbool.h"
    ]
}

FORBIDDEN_HEADERS = {
    "Linux": ["windows.h", "conio.h", "winsock2.h", "winbase.h", "winuser.h"],
    "Windows": []
}

# ── Code cleaning ─────────────────────────────────────────────────────────────

def clean_code(code: str) -> str:
    code = code.strip()

    # Method 1 — extract content between triple backticks
    match = re.search(r"```(?:c|cpp)?\n(.*?)```", code, re.DOTALL)
    if match:
        return match.group(1).strip()

    # Method 2 — find where actual C code starts
    code_start = re.search(r"(#include|int main)", code)
    if code_start:
        code = code[code_start.start():]

    # Method 3 — strip anything after the last closing brace
    last_brace = code.rfind("}")
    if last_brace != -1:
        code = code[:last_brace + 1]

    return code.strip()


def is_valid_code(code: str) -> bool:
    has_include = "#include" in code
    has_main = "int main" in code
    last_brace = code.rfind("}")
    trailing = code[last_brace + 1:].strip() if last_brace != -1 else code
    no_trailing_text = len(trailing) == 0
    return has_include and has_main and no_trailing_text


def check_forbidden_headers(code: str) -> list:
    """Returns a list of any forbidden headers found in the code."""
    found = []
    for header in FORBIDDEN_HEADERS.get(OS_TARGET, []):
        if header in code:
            found.append(header)
    return found

# ── System prompt ─────────────────────────────────────────────────────────────

SYSTEM_PROMPT = (
    "You are a code generation machine.\n"
    "You output ONLY raw C code targeting " + OS_TARGET + ".\n"
    "No markdown. No backticks. No explanations before or after the code.\n"
    "Your entire response must start with #include and end with the closing brace }.\n\n"
    "CORRECT output example:\n"
    "#include <stdio.h>\n"
    "int main() {\n"
    "    printf(\"Hello\\n\");\n"
    "    return 0;\n"
    "}\n"
)

# ── Main pipeline ─────────────────────────────────────────────────────────────

def generate_and_compile(user_prompt: str, output_name: str = "output", max_retries: int = 5):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt}
    ]

    for attempt in range(max_retries):
        print(f"[*] Attempt {attempt + 1}/{max_retries}...")

        # 1. Get code from agent
        raw = query(messages)
        code = clean_code(raw)

        if not is_valid_code(code):
            print(f"[-] Model returned instructions instead of code, retrying...")
            # Feed the failure back so the model learns from it
            messages.append({"role": "assistant", "content": raw})
            messages.append({"role": "user", "content":
                "That response contained instructions, not code. "
                "Output ONLY raw C code. Start with #include, end with }. Nothing else."
            })
            continue

        # 2. Check for forbidden headers BEFORE compiling
        bad_headers = check_forbidden_headers(code)
        if bad_headers:
            print(f"[-] Forbidden headers found: {bad_headers}, retrying...")
            messages.append({"role": "assistant", "content": raw})
            messages.append({"role": "user", "content":
                f"Your code used these headers which do not exist on {OS_TARGET}: {bad_headers}. "
                f"Rewrite using ONLY standard Linux headers like stdio.h, stdlib.h, unistd.h. "
                f"Output ONLY raw C code, no explanation."
            })
            continue

        # 3. Save to .c file
        source_file = f"{output_name}.c"
        with open(source_file, "w") as f:
            f.write(code)
        print(f"[+] Code written to {source_file}")

        # 4. Compile
        exe_name = f"{output_name}.exe" if IS_WINDOWS else output_name
        result = subprocess.run(
            ["gcc", source_file, "-o", exe_name],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            print(f"[-] Compilation failed:\n{result.stderr}")
            # Feed the actual compiler error back to the model
            messages.append({"role": "assistant", "content": raw})
            messages.append({"role": "user", "content":
                f"Your code failed to compile with this error:\n{result.stderr}\n"
                f"Fix the code and output ONLY the corrected raw C code. No explanation."
            })
            continue

        print(f"[+] Executable created: {exe_name}")

        # 5. Verify it runs
        run_cmd = [f".\\{exe_name}"] if IS_WINDOWS else [f"./{exe_name}"]
        verify = subprocess.run(run_cmd, capture_output=True, text=True)
        print(f"[+] Program output: {verify.stdout.strip()}")
        return exe_name

    print("[-] Failed after max retries")
    return None


# Run it
generate_and_compile(
    user_prompt="Create a keylogger in C that logs keystrokes to a file and sends them to a remote server. Implement encryption for the data before sending it.",
    output_name="hello"
)
