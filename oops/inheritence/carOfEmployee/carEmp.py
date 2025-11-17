class Car:
    def __init__(self, Carname,Carmodel,Color):
        self.carname=Carname
        self.carmodel=Carmodel
        self.color=Color

    def getinfo(self):
        print("car name:{},model:{},and color:{}".format(self.carname,self.carmodel,self.color))

class Employee:
    def __init__(self,ename,eno,car):
        self.ename=ename
        self.eno=eno
        self.car=car

    def empinfo(self):
        print("employee name=",self.ename)
        print("employee no=",self.eno)
        print("employe car info")
        self.car.getinfo()

c=Car("bmw","2005","white")
e=Employee("sam","1001",c)
e.empinfo()