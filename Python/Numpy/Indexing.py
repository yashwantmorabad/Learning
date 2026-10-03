#Array indexing
import numpy as np
x=np.array([1,2,3,4,5])
print(x)
print(type(x))
print(x[4])
print(x[0]+x[2])

#2-Dimension array
b=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(b)
print(b[0,0])

#3-Dimensional or multi-dimensional array
c=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(c)
print(c.ndim)
print(c[0,0,1])

