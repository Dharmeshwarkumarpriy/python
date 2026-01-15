import threading
from threading import Thread, active_count


def display():
    for i in range(1,11):
        print('child thread \n')
        print(threading.Thread)
t=Thread(target=display)
t.start()

t1=Thread(target=display)
t1.start()
t2=Thread(target=display)
t2.start()
t3=Thread(target=display)
t3.start()
t4=Thread(target=display)
t4.start()
print("active thread =",active_count())