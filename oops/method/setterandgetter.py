class Student:
    def setName1(self,name1):
        self.name1=name1

    def setRoll1(self,roll1):
        self.roll1=roll1



    def getName1(self):
        return self.name1

    def getRoll1(self):
        return self.roll1

n= int(input("enter no of student:"))

for i in range(n):
    s = Student()
    name1=input("enter student name:")
    roll1=input("entet student roll:")
    s.setName1(name1)
    s.setRoll1(roll1)

    print(s.getName1(),s.getRoll1())
    print(s.getRoll1())