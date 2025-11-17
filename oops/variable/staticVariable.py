class Test:
    x=10
    def __init__(self):
        self.y=20


t1=Test()
t2=Test()
print("t1:",t1.x,t1.y)
print("t2",t2.x,t2.y)
#t1.y=999
Test.x=888
print("t1:",t1.x,t1.y)
print("t2:",t2.x,t2.y)