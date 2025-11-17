a=input("enter the 1st value:")
b=input("enter the 2st value:")
c=input("enter the 3st value:")
max =a if a>b and a>c else b if b>c else c
print("max value=",max)
print(type(max))