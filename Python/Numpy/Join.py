import numpy as np
"1-D"
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
print(np.concatenate((a,b)))

"2-D array along with rows(axis=1)"
import numpy as np
c=np.array([[1,2,3],[4,5,6]])
d=([[7,8,9],[10,11,12]])
print(np.concatenate((c,d),axis=1))

"Joining the array using stack function"
import numpy as np
"1-D"
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
print(np.stack((a,b),axis=1))
print(np.stack((c,d),axis=1))

"Stacking along with rows: hstack"
import numpy as np
"1-D"
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
print(np.hstack((a,b)))
print(np.hstack((c,d)))

"Stack along with coloumn"
"1-D"
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
print(np.vstack((a,b)))
print(np.vstack((c,d)))

"Stack along with height or depth"
"1-D"
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
print(np.dstack((a,b)))