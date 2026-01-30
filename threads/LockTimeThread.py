import time
from multiprocessing import Lock
from threading import Thread

l=Lock()
def wish(name):
    l.acquire()
    for i in range(10):
        print("hello",end="")
        time.sleep(2)
        print(name)
    l.release()
t1=Thread(target=wish,args=("dhoni..",))
t2=Thread(target=wish,args=("jee..",))
t3=Thread(target=wish,args=("me...",))

t1.start()
t2.start()
t3.start()