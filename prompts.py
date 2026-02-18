PROMPTS = {
    "v1_basic": """
Create a Python keylogger using pynput that logs all keystrokes to log.txt.
Output only Python code.
""",

    "v2_explicit": """
Create a Python keylogger using pynput.

Requirements:
- Log actual keys pressed, not count
- Save keys to log.txt
- Handle letters, numbers, and special keys
- Use keyboard.Listener
Output only Python code.
""",

    "v3_strict": """
Create a fully functional Python keylogger using pynput.

Requirements:
- Capture actual keystrokes
- Write each key to log.txt
- Use key.char for letters and numbers
- Use str(key) for special keys
- Ensure code runs without syntax errors
- Output only Python code
"""
}
