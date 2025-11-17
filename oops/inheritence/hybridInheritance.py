# hybrid inheritance ....
class A:
    def m1(self):
        print("class-A method")

class B:
    def m2(self):
        print("class=B ")

class C:
    def m3(self):
        print("class-C")

# multiple inheritance ...
class D(A,B,C):
    def m4(self):
        print("class-D")

class E(D):
    def m5(self):
        print("class-E")

class F(D):
    def m6(self):
        print("class-F")

class G(D):
    def m7(self):
        print("class-G")

d=D()
d.m1()
d.m3()
g=G()
g.m1()