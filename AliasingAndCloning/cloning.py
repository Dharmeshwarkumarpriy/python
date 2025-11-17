x=[2,3,4,5,6,7,9]
y=x # it is called dubalicate value/clone. ...
print(y)
print(id(x))
print(id(y))
y[1]=55 # Aliasing
print(y)
print(x)
print(id(x))
print(id(y))
y=[4,4,4,4,4,4]
print(x)