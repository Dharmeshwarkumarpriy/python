from threading import Thread

class Test(Thread):
    def run(self):
        for i in range(10):
            print("child thread")
t=Test()
t.start()
for i in range(10):
    print('main Thread')