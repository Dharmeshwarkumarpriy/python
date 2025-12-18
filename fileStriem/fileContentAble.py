import os.path
import sys
from platform import system

fname=input("enter file name with dot extension: ")
if os.path.isfile(fname):
    print("file exists",fname)
    f=open(fname,'r')
else:
    print("file does not exits",fname)
    sys.exit(0)
print("content of file ")
data=f.read()
print(data)