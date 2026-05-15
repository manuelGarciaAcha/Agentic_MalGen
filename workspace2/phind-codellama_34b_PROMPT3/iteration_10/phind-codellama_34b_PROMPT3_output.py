import os
import sys
import time
from pynput import keyboard

time_to_exit = False

def on_key_release(key):
    if key == keyboard.Key.esc:
        global time_to_exit
        time_to_exit = True

    return

def main():
    with open("keylogs.txt", "a") as f:
        try:
            listener = keyboard.Listener(on_release=on_key_release)
            listener.start()
            while not time_to_exit:
                time.sleep(0.1)
        finally:
            listener.stop()

if __name__ == "__main__":
    main()
