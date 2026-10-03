#Breaking the array
"1-D"
import numpy as np
# x=np.array([1,2,3,4,5,])
# print(np.array_split(x,2))
# print(np.array_split(x,2)[0])#It gives the element at index 0

# print(np.array_split(x,3))
# print(np.array_split(x,3)[0])
# print(np.array_split(x,4))
# print(np.array_split(x,4)[0])

"2-D"
# import numpy as np
# y=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# print(np.array_split(y,2))
# print(np.array_split(y,2)[0])
# print(np.array_split(y,2)[1])

# print(np.array_split(y,3))
# print(np.array_split(y,3)[0])
# print(np.array_split(y,3)[1])
# print(np.array_split(y,3)[2])

# print(np.array_split(y,4))
# print(np.array_split(y,5))
# a=np.array_split(y,5)
# b=[[13,14,15]]
# a[4]=np.append(a[4],[[13,14,15]],axis=0)
# print(a)

"hsplit()"
z=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(np.hsplit(z,3))