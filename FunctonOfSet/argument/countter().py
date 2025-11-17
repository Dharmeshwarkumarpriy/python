def counter(n):
    print("coundown start")
    while n>0:
        yield n
        n=n-1

    values=counter(6)
    for x in values:
        print(x)