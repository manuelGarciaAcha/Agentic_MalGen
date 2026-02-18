import logging
from pynput import keyboard


class MyKeyBoardListner(keyboard.Listener):
    """Listener Class"""

def __init__(self, logger_param):
    self.logger = logger_param()
    self._keys_pressed = {}


def on_press(self, key):
    if key not in self._keys_pressed:
        self._keys_pressed[key] = 0
    self._keys_pressed[key] += 1
    logging.debug("Pressed: %s", str(key))

def release(self, key):
    """Released: %s"% (str(key)))
   s"""
    if key in self._keys_pressed:
        self._keys_pressed[key] -= 1
    else:
        self.logger.warning("Pressed twice on %s", (str(key)))

def get_pressed(self):
    return list(self._keys_pressed)

logging.basicConfig(filename='logFile.txt', filemode='w')
listener = MyKeyBoardListner(logging.RootLogger().propagate==False)
with keyboard.Events() as events:
     listener.join()