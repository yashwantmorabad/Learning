"Permutation can be done by two method"
from numpy import random
import numpy as np
a=np.array([1,2,3,4,5])
random.shuffle(a)#This will shuffle the array in place
print(a)

b=np.array([1,2,3,4,5])
print(random.permutation(b))
print(b)