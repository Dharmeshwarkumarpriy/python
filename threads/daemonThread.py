# the thread which are running in the background are called Daemon Threads.
# the main objective of daemon threads is to provide support for non-Daemon Thread.
from threading import Thread, current_thread


def display():
    print("started thread")
t1=Thread(target=display())
t1.start()
print(current_thread())
print(current_thread().isDaemon())

# note:- main thread is always non-daemon and we can not change its daemon nature because it is already started as the begining.