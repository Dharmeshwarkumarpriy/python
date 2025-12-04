try:
    x = int(input("enter the value of x= "))
    y = int(input("enter the value of y= "))
    print(x / y)
except (ZeroDivisionError,ArithmeticError,ValueError):
    print("invalid statement in program:")