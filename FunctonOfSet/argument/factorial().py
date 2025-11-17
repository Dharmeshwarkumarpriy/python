def fact(n):
    if n==0:
        result=1
        print(result)
    else:
        result=n*fact(n-1) ## 5*4*3*2*1=120
        print(result)
    return result
print("factorial=",fact(5))