#Numpy datatypes
import numpy as np
x=np.array([1,2,3,4,5])
print(x.dtype)
y=np.array(['1','2','3','4','5'])
print(y.dtype)
z=np.array(['Apple','Banana','Mango'])
print(z)
print(z.dtype)

# x=np.array([1,2,3,4,5],dtype='S')
# print(x)
# print(x.dtype)

#if we enter data with diffrent datatype then 
# it will raise error 
# x=np.array([1,2,3,4],dtype='i4')
# print(x) 
# print(x.dtype)

#Conversion of datatype we use .dtype function
# x=np.array([1.1,2.3,3.1,4.6,5.8])
# print(x) 
# print(x.dtype)
# y=x.astype('i')
# print(y) 
# print(y.dtype)

#Difference copy and view of an array
import numpy as np
# x=np.array([1,2,3,4,5,])
# y=x.copy()
# y[0]=10
# print(x)
# print(y)

# x=np.array([1,2,3,4,5,])
# y=x.view()
# y[0]=10
# print(x)
# print(y)