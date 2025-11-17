x=20
y=30
g=x,y

# show1
print("show1...")
def show1():
    print(x,y)
show1()

# show2
print("show2...")
def show2():
    z=40
    s2=x,y,z
    print(s2)
    print(x,y,z)
show2()

# show3
print("show3...")
def show3():
    print(g)
    print(x,y)
show3()