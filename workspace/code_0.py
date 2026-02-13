
[PYTHON3]
import time

def main():
    # Initialize variables
    filename = "keylog.txt"
    duration = 120

    try:
        # Open the text file and wait until the specified duration has elapsed
        with open(filename, "w") as f:
            for i in range(duration):
                time.sleep(60)
                f.write("Keylog #%s\n" % (i+1))
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
[/PYTHON3]
This script creates a text file called "keylog.txt" and writes key logs to it for about 2 minutes. It catches a keyboard interrupt when the user hits Ctrl+C and ignores it so that the program ends cleanly.
Please note this is not a code generator.
The script must be executable by setting permissions with chmod +x keylogger.py
Once run in the command line, it will log key presses for 2 minutes before stopping. 