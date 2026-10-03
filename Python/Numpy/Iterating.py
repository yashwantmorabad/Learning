import numpy as np
"1-D"
n=np.array([1,2,3,4])
print(n)
for i in n:
    print(i)

"2-D"
import numpy as np
o=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(o)
print(o.ndim)
for j in o:
    print(j)

"Iterate on each scalar element on 2-D array"
o=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
for m in o:
    for n in m:
        print(n)

"3-D"
import numpy as np
z=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21],[22,23,24],[25,26,27]]])
print(z.ndim)
for a in z:
    print(a)
for b in z:
    for c in b:
        for d in c:
            print(d)

'''To access each element no. of dimension is equal to
no. of nested for loops'''