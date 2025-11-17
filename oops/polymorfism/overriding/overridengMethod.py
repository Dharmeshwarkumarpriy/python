class Test:
    def m1(self):
        print("no-org method")

    def m1(self,a,b):
        print("two-org method")

    def m1(self,c,d):
        print("two-org meth")

t=Test()
#t.m1()
#t.m1(89)
t.m1(90,80)