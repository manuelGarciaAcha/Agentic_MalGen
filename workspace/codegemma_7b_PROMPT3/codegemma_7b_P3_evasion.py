from pynput import mouse

logging.basicConfig(filename="mouselogs.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

def on_click(x, y, button, pressed):
    try:
        logging.info(f"{button} clicked at ({x}, {y})")
    except Exception as e:
        logging.error(f"Error logging click: {e}")

listener = mouse.Listener(on_click=on_click)
listener.start()

while True:
    pass