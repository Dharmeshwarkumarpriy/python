import sys
import time
from sys import getrefcount


class Test:
    def __init__(self):
        print("object initialization")
    def __del__(self):
        print("class up activities perform")

t1=Test()
t1=None
time.sleep(5)
print("end of application")
print(sys.getrefcount(t1))