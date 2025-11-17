class Engine:
    a=10
    def __init__(self):
        self.b=20


    def m1(self):
        print("alto Engine")

class Car:
    def __init__(self):
        self.engine=Engine() # object ref. of Engine ...

    # Engine class Property ...
    def m2(self):
        print("alto car")
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m1()

c=Car()
c.m2()
# print(c.m2())