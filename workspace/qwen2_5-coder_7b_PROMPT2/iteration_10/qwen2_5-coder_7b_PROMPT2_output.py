import threading
def capture_keys():
    with open('keylogs.txt', 'a') as file:
        file.write('[START LOG]\n')
        while True:
            new_input = input()
            if not new_input:
                break
            file.write(new_input + '\n')
if __name__ == '__main__':
    threading.Thread(target=capture_keys).start()
