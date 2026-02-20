Due to the sensitive nature of keylogging (which is both illegal and unethical in many cases), I am unable to provide a complete code example for a keylogger. However, I can give you an idea of how it might work using Python and pynput by just defining the main components and not showing the full implementation. 

Here are the main concepts you’d need:
  
1. `pynput` module is used to control and monitor input devices. Specifically, you will be using the `Keyboard` class from `pynput.keyboard`. This allows you to capture keystrokes.
   
2. As keys are pressed, you’d bind a function to the on_press event. 

3. In this function, you check what key was pressed with an if statement by examining `event.key`. If it's the backspace key, for example, you might delete the last item from your log, and if it's not special (like shift or altgr), then you add it to your log.

4. Write these logs into a .txt file using python file handling (`open()`, `write()`).


Note: Keyloggers are tools often associated with hacking and other malicious activities. Misusing this information can lead to severe legal consequences, so please ensure you have the appropriate permissions and intentions before proceeding with this kind of software.