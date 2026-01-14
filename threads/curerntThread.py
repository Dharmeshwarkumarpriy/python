import threading
from threading import Thread, current_thread

# for getName use .name ....
# getName() = name for attribute ....
print("current executing thread:",threading.current_thread().name)

# for setName use .name="sam" ...
# setName() = name="as" for setting ...
current_thread().name="sam"
print("current executing thread:",current_thread().name)

def test():
    print("child thread")
t=Thread(target=test())
t.start()
print("id no of main thread=",current_thread().ident)
print('child thread id=',t.ident)