class Test:
    x=10
    _y=20
    __z=30
    def m1(self):
        print(Test.x)
        print(Test._y)
        print(Test.__z)
    def m2(self):
        print(Test.__z)

class C(Test):
    def m3(self):
        print("z value",C._y)

c=C()
c.m1()
c.m2()
c.m3()
print(Test.x)
print(Test._y)
print("outside of class =",c._Test__z)