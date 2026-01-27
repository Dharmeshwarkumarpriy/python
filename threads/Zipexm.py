import time
from threading import Semaphore, Thread

s=Semaphore(2)
def wish(name):
    s.acquire()
    for i in range(10):
        print("hi thread:",end="")
        time.sleep(3)
        print(name)
    s.release()

t1=Thread(target=wish,args=("sam",))
t2=Thread(target=wish,args=("raj",))
t3=Thread(target=wish,args=("rajesh",))
t4=Thread(target=wish,args=("raju",))
t5=Thread(target=wish,args=("ramesh",))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()