try:
    print(19.5/0)
    print(0/0)
    print(10/0)
except ZeroDivisionError:
    print(20/2)

# default except most be lase ...
except:
    print("default exception")