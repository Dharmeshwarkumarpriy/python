# a=1,2,3,4,5,6,7
# s: str=str(a)
# s.polyval(s)
# print(a)
import numpy as np

poly = [1,2,3,4,5,6,7] # Coefficients
x = 2 # Value of x
print(np.polyval(poly, x))
print(np.invert(poly))


# new....
poly = [1,2,3,4,5,6,7]   # Coefficients
x = 1   # Value of x

res = 0 # Initialize result
for i in poly:
    res = res * x + i
print(res)


#..............
import numpy as np

a = np.arange(5)
r = a * 10    # Vectorized operation (fast and efficient)
print(r)

#..........
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
x = 10
print(a + x)

#...............
import numpy as np
arr = np.array([1, 2, 3])
res = arr + 1
print(res)

#...............
import numpy as np

a = np.array([2, 4, 6])
b = np.array([[1, 3, 5], [7, 9, 11]])
res = a + b
print(res)
m=np.min(b)
print("min=",m)
mx=np.max(b)
print("max=",mx)
li=np.mean(b)
print(li)
w=np.where(b>50)
print(w)

lo=np.log(b)
print("log=",lo)

sp=np.sqrt(a)
print("sqet=",sp)

#.................
import numpy as np

a = np.array([12, 24, 35, 45, 60, 72])
b = np.array(["Adult", "Minor"])
res = np.where(a > 18, b[0], b[1])
print(res)

#..........
eigenvalue,eigenvertor=np.linalg.eig(np.array([[1,2],[2,1]]))
print(eigenvalue,eigenvertor)

#...........
randomInt=np.random.randint(0,10,5)
print(randomInt)

#..............
