class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30

    def m1(self):
        del self.c
t=Test()
print(t.__dict__)
t.m1()
print(t.__dict__)
del t.a
print(t.__dict__)
# print(t.dict)
# print(t)
# print(t.c)
# print(t.__int__())
# print(t.mi())
# t.__int__()
