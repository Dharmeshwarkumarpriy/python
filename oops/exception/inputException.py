try:
    x=int(input("enter the value of x="))
    y=int(input("enter the value of y="))
    print(x/y)
except ArithmeticError:
    print("arithmetic arror")