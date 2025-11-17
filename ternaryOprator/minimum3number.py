a=int (input("enter the 1st value:"))
b=int (input("enter the 2st value:"))
c=int (input("enter the 3st value:"))
min =a if a<b and a<c else b if b<c else c
print("minimum value=",min)
print(type(min))