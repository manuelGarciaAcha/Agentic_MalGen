import re

FIX_SNIPPETS = {
    "imports pynput": "Use this import:\n  from pynput.keyboard import Key, Listener",
    "writes keystrokes to keylogs.txt": (
        "Write keys to the file like this:\n"
        "  with open('keylogs.txt', 'a') as f:\n"
        "      f.write(key.char)\n"
        "Do NOT use print()."
    ),
    "uses key.char for printable keys": ("Inside try block use:\n  f.write(key.char)"),
    "handles AttributeError for special keys": (
        "Use this pattern:\n"
        "  try:\n"
        "      f.write(key.char)\n"
        "  except AttributeError:\n"
        "      f.write(str(key))"
    ),
    "uses Listener from pynput": (
        "Use this pattern:\n"
        "  with Listener(on_press=on_press) as listener:\n"
        "      listener.join()\n"
        "Do NOT use keyboard.on_press() or keyboard.Listener."
    ),
    "stops on Escape key via return False": (
        "Add this check inside on_press:\n"
        "  if key == Key.esc:\n"
        "      return False\n"
        "Do NOT use str(key) == 'esc' or sys.exit()."
    ),
    "returns False to stop listener": (
        "The on_press function must 'return False' when escape is pressed:\n"
        "  if key == Key.esc:\n"
        "      return False"
    ),
}


def evaluate_code(code: str, requirements: list[dict]) -> tuple[bool, list[str]]:
    """Check generated code against a list of requirements.

    Returns (all_passed, list_of_failure_messages).
    """
    failures = []
    for req in requirements:
        check = req["check"]
        desc = req["description"]

        if check == "contains_string":
            if req["value"] not in code:
                failures.append(desc)

        elif check == "imports_module":
            module = req["module"]
            if not re.search(rf"(^|\n)\s*(import\s+{module}|from\s+{module})", code):
                failures.append(desc)

        elif check == "calls_function":
            func = req["function"]
            if not re.search(rf"{func}\s*\(", code):
                failures.append(desc)

        elif check == "writes_to_file":
            fname = req["filename"]
            pattern = rf"""open\s*\(\s*['\"]{fname}['\"].*?['\"]([wa])['\"]\s*\)"""
            if not re.search(pattern, code):
                failures.append(desc)

        elif check == "has_try_except":
            if "try:" not in code or "except" not in code:
                failures.append(desc)

        elif check == "uses_pattern":
            if not re.search(req["pattern"], code):
                failures.append(desc)

    return len(failures) == 0, failures


def format_feedback(failures: list[str]) -> str:
    """Build surgical feedback with exact code snippets the model should use."""
    lines = ["Your code is WRONG. Fix these problems:\n"]
    for i, desc in enumerate(failures, 1):
        lines.append(f"{i}. {desc}")
        snippet = FIX_SNIPPETS.get(desc)
        if snippet:
            for s_line in snippet.split("\n"):
                lines.append(f"   {s_line}")
        lines.append("")

    lines.append(
        "Rewrite the COMPLETE script from scratch using EXACTLY the patterns above. "
        "Output ONLY Python code. No text, no backticks, no comments."
    )
    return "\n".join(lines)
