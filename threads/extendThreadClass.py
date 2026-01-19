from threading import Thread


class Test:
    def display(self):
        for i in range(10):
            print("child class")
Obj=Test()
t=Thread(target=Obj.display)
t.start()
for i in range(10):
    print("main thread")