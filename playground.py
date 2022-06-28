import numpy as np


x = np.array([1,2,3])
y = [7,8,9]
q = np.insert(x,1,y)
print(x)
print(q)
x[1] = y
print(x)