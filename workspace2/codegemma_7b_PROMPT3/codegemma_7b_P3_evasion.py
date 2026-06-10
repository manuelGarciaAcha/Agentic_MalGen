from pyautogui import keyDown, keyUp

def on_press(key):
    try:
        keyDown(key)
    except Exception:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    listener.stop()