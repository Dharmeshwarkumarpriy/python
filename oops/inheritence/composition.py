class Student:
    collegeName= "tancollage"

    def __init__(self, name):
        self.name = name


print(Student.collegeName)
s = Student("sam")
print(s.name)
#print(s.collegeName)
