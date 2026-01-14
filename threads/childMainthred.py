import threading
from threading import Thread, active_count


def display():
    for i in range(1,11):
        print('child thread \n')
        print(threading.Thread)
t=Thread(target=display)
t.start()

for i in range(1,11):
    print("main thread")