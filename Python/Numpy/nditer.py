"We use this function to iterate the each single element"
"3-D"
'''Number of elements in each square bracket should be equal'''
'''We can use indexing as well in nditer function to access specific elememts'''
import numpy as np
z=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21],[22,23,24],[25,26,27]]])
print(z.ndim)
for a in z:
    print(a)
for b in z:
    for c in b:
        for d in c:
            print(d)

for i in np.nditer(z):
    print(i)

"2-D"
import numpy as np
o=np.array([[1,2,3,3],[4,5,6,6],[7,8,9,9],[10,11,12,12]])
for n in np.nditer(o[:,:3]):
    print(n)
    