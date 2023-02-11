from pynput.keyboard import Key,Listener
def li(key):
    print(key)
with Listener(on_press=li) as listener:
    listener.join()