import numpy as np
a=np.array([1,2,3,4])
b=np.array([True,False,True,False])
print(a[b])

import numpy as np
c=np.array([1,2,3,4,5,6,7,8,9,10])
d=[]
for i in c:
    if i<6:
        d.append(True)
    else:
        d.append(False)
print(d)
print(c[d])
e=c<6
print(c[e])
print(c[c < 6])
"Same as above two line but it is slow"
# The slow way (Standard Python)
result = [x for x in c if x < 6]
print(result)