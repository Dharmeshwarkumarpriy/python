try:
    x=int(input("enter the value of x="))
    y=int(input("enter the value of y="))
    print(x/y)
except ArithmeticError:
    print("arithmetic arror")
except ZeroDivisionError:
    print("we can not divice with zero")
except ValueError:
    print("plesse enter valid value")

except ValueError:
    print("statement-5")
except EnvironmentError:
    print("environment-6")
except IndexError:
    print("index error-7")