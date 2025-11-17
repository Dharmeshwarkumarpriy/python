x=[23,34,45,56,67,78]
y=x[:] # cloning using slicing. ....
y[1]=788
print(y)
print(x)
print(id(y))
print(id(x))