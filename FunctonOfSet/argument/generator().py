def firstn(n):
    n=1
    while a<=0:
        yield a
        a=a+1

    #  we can convert generator into list as follows...

values=firstn(10)
l1=list(values)
print(l1)