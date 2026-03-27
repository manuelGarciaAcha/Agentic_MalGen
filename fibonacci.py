import logging
import sys

def log_keys():
    logger = logging.getLogger('Key Logger')
    logger.setLevel(logging.INFO)
    
    handler = logging.FileHandler('keylog.txt', encoding='utf-8')
    handler.setFormatter(logging.Formatter('%(asctime)s: %(message)s'))
    
    logger.addHandler(handler)

    while True:
        for key_event in sys.stdin:
            if 'ASCII' not in key_event:
                continue
            
            _, key = key_event.split() 
            logger.info(f"Key pressed: {key}")

if __name__ == "__main__":
    log_keys()