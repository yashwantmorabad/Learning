#shape of an array-the number of
#element in each dimensions
import numpy as np
b=np.array([[1,2,3,4,5],[6,7,8,9,10],[5,4,3,2,1],[10,9,8,7,6]])
print(b.shape)
print(b.ndim)

e=np.array([1,2,3],ndmin=5)
print(e)
print(e.shape)
# print(e.ndim)