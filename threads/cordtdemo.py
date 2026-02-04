from asyncio import Condition
from threading import Thread


def consume(c):
    c.wait()
    print("consumer got notification and consuming item")
    c.release()

def producer(c):
    c.acquire()
    print("producer producing item")
    print("producer giving notification")
    c.notify()
    c.release()

c=Condition()
t1=Thread(target=consume,args=(c,))
t2=Thread(target=producer,args=(c,))
t1.start()
t2.start()