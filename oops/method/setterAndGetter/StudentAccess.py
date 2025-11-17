from oops.method.setterAndGetter.Student import Student as Students
n=int(input("enter the no. of student record:"))
for i in range(n):
    s=Students()
    stuName=input("enter the name of student:")
    stuAge=input("enter the age of student:")
    stuAddress=input("enter the address of student:")
    s.setStudentName(stuName)
    s.setStudentAge(stuAge)
    s.setStudnetAddress(stuAddress)

    print("hi..",s.getStudentName(),s.getStudentAge(),s.getStudentAddress())