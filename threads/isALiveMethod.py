from threading import Thread

def display():
    print("started thread")
t1=Thread(target=display())
t1.start()
# is_alive() is check thread is executed or not. ...
print(t1.is_alive())