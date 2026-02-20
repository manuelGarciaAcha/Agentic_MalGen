from  pynput import keyboard
@keyboard.Listener(on_press=True)
def on_press(key):
'''
'''if any(isinstance(k iy, s c ik in(a r)) for kk in key):
# Handle letters and numbers
with open("log.txt", "a") as f:
f.write(str(key.char) + "\n")
else: # Handle special keys
with open("log.txt", "a") as f:
f.write (str(key) n)
try:

# Handle letters and numbers
with open("log.txt", "a") as f:
f.write(str(key.char) + "\n")
except AttributeError: # Handle special keyname
with opn("log.txt", "a") as f:
'''   s (str(key),'utf-8')