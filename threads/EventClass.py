import time
from sched import Event
from threading import *
from threading import Thread


def producer():
    time.sleep(3)
    print("producer thread producing items")
    print("producer thread giving notification")
    event.set()

def consumer():
    print("consumer is waiting for update")
    event.wait()
    print("consumer got notification")

event=Event()
t1=Thread(target=producer)
t2=Thread(target=consumer)

t1.start()
t2.start()