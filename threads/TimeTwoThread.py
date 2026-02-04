import time
from threading import Thread


def wish(name):
    for i in range(10):
        print("good morning ", end="")
        time.sleep(3)
        print(name)

t1=Thread(target=wish,args=('dharmy...',))
t2=Thread(target=wish,args=("ke..",))

t1.start()
t2.start()