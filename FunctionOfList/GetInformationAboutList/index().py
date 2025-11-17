l=[1,2,2,3,3,1,4,4,"2,3,4,5"]
# check first index occurrence of element. ...
print(l.index(1))
print(l.index(2))
print(l.index(3))
print(l.index(4))

print(l.index("2"))
# valueError: 6 is not in list. ...
print(l.index(6))