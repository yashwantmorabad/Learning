'''You are allowed to have only one
dimension'''
import numpy as np
n=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
m=n.reshape(2,2,-1)#-1 represents the unkown dim acc to need
print(m)
print(m.ndim)

'''Faltrening the array by converting multidimesional
array in 1-D'''
import numpy as np
m=np.array([[1,2,3],[4,5,6]])
n=m.reshape(-1)
print(n)