from threading import Condition, Thread

def parent(c):
    c.acquire()
    print("Parent is waiting for teacher")
    c.wait()
    print("parent meet teacher and discuss about their child")
    c.release()

def teacher(c):
    c.acquire()
    print("teacher is taking class")
    print("teacher finishes class")
    c.notify()
    c.release()

c=Condition()
t1=Thread(target=parent,args=(c,))
t2=Thread(target=teacher,args=(c,))
t1.start()
t2.start()