import csv

with open('Student.csv',"w",newline='') as f:
    w=csv.writer(f)
    w.writerow(['student name',"course",'roll no','phone no','DOB','address'])
    n=int(input('enter the no of student:'))

    for i in range(n):
        stuName=input('enter the student name=')
        course=input('enter the course=')
        rollNo=input('enter the rol no=')
        phoneNo=input('enter the phone no=')
        date=input('enter the date of birth=')
        address=input('enter the address=')
        w.writerow([stuName,course,rollNo,phoneNo,date,address])
print('total data added.')