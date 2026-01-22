from threading import BoundedSemaphore, Semaphore

# BoundedSemaphore allow acquire() = release() ...
b=BoundedSemaphore(2)
b.acquire()
b.acquire()

b.release()
b.release()
print("end BoundedSemaphore")


s=Semaphore(2)
# it many allow to release() ....
s.acquire()
s.acquire()

s.release()
s.release()
s.release()
s.release()
print("end semaphore")