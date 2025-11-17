x=[12,32,34,45,65,67,78]
y=x.copy() # cloning using copy() method. ...
y[1]=828
print(y)
print(x)
print(id(x))
print(id(y))