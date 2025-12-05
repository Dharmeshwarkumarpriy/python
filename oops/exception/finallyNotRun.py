import os

try:
    print("start 1")
    os._exit(0)
    print("start 2")
    try:
        print("start 3")
        print("start 4")
    except:
        print("start 5")
    finally:
        print("start 6")
    print("start 7")
except ZeroDivisionError:
    print("start 8")
except:
    print("value exception")
finally:
    print("start 9")
print("start 10")