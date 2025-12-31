a=int(input("enter year:"))
if a%4==0 & a%100!=0 | a%400==0:
    print('leap year.')
else:
    print('not leap year.')