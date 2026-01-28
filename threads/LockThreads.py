from multiprocessing import Lock

l=Lock()
print("main thread typing to acquire")
l.acquire()
print("main thread try to acquire again")
l.release()