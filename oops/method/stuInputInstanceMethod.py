class Student:
    def __init__(self,name1,clas1,roll1): # instance method...
        self.name=name1
        self.clas=clas1
        self.roll=roll1

    def display(self):
        print("hello...",self.name,self.clas,self.roll)

s=Student(name1=input("enter stu name:"), clas1=input("enter class:"),roll1=input("enter roll:"))
s.display()