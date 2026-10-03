'''Reshaping means changing the shape of the array
like adding or removing elements'''
"From 1-D to 2-D"
import numpy as np
m=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
n=m.reshape(4,3)
print(n)

"From 2-D to 3-D"
import numpy as np
s=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
t=s.reshape(2,3,2)
print(t)
print(t.ndim)