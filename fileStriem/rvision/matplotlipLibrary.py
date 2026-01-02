import matplotlib.pyplot as plt
import numpy as np

xPoints=np.array([0,6,7,8,9])
yPoints=np.array([3,12,45,65,87])
plt.plot(xPoints,yPoints)

plt.xlabel("year")
plt.ylabel("sale")
plt.plot(xPoints,yPoints,color='r')
#plt.title("line chart",marker='r')
plt.scatter(xPoints,yPoints,color='g',marker='*',s=100)
plt.bar(xPoints,yPoints)
plt.show()
