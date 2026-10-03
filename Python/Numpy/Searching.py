import numpy as np
a=np.array([1,2,3,4,5,4,3,1])
print(np.where(a==4))

"Finding index"
b=np.array([1,2,3,4,5,6,7,8])
print(np.where(b%2==0))
print(np.where(b%2!=0))

"Searchsorted()-Performs binary seach in array"
c=np.array([1,2,3,4,5,6,7,8,9,10])
print(np.searchsorted(c,7))
print(np.searchsorted(c,7,side='right'))

"Search multiple index of different elements"
d=np.array([1,3,5,7])
e=(np.searchsorted(d,[2,4,6,8]))
print(e)
print(d)