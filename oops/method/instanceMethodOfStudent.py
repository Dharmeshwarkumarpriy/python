class Student:
    def __init__(self,name1,clas1,roll1,marks1): # instance method...
        self.name=name1
        self.clas=clas1
        self.roll=roll1
        self.marks=marks1

    def display(self):
        print("hello...",self.name,self.clas,self.roll,self.marks)


s=Student(name1="dharmy", clas1="mca",roll1=240003020005,marks1=80.7)
s.display()

# taking by user input...
s1=Student(name1=input("enter stu name:"), clas1=input("enter class:"),roll1=input("enter roll:"),marks1=input("enter marks:"))
s1.display()