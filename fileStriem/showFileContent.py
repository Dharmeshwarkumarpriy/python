import os.path
import sys

fname=input("enter file Name:")
if os.path.isfile(fname):
    print("file exists",fname)
    f=open(fname,'r')
else:
    print('file does not exist',fname)
    sys.exit(0)
l_count=0
w_count=0
c_count=0
for line in f:
    l_count=l_count+1
    c_count=c_count+len(line)
    word=line.split()
    w_count=w_count+len(word)
    print(word)
    print(l_count,c_count,w_count)