from pynput import mouse

logging.basicConfig(filename="mouselogs.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

def on_click(x, y, button, pressed):
    logging.info(f"{button} clicked at ({x}, {y})")

listener = mouse.Listener(on_click=on_click)
listener.start()

while True:
    pass