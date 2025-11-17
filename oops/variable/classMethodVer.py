class Test:
    a=80
    @classmethod
    def m1(cls):
        del cls.a

Test.m1()
print(Test.__dict__)
def m2():
    Test.c=80
    del Test.c
print(Test.__dict__)