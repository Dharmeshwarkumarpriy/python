class Test:

    def m2(self):
        x=80
        print(x)

    x=90 # instance variable.

    def m1(self):
        a=100 # local variable.
        print(a)
t=Test()
t.m1()
print(Test.x) # unresolve referance x.


t=Test()
t.m2()