from threading import Thread

def job():
    print("child thread")
t=Thread(target=job())

#print(t.isDaemon())
print(t.daemon)

#t.setDaemon(True)
t.daemon=True

#print(t.isDaemon())
print(t.daemon)