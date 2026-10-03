import numpy as np
x=np.array([1,2,3,4,5])
print(x)
print(type(x))

y=np.array((1,2,3,4,5))
print(y)
print(type(y))

#Dimensions in array
#0-Dimension array
a=np.array(27)
print(a)

#1-Dimension array
y=np.array((1,2,3,4,5))
print(y)

#2-Dimension array
b=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(b)

#3-Dimensional or multi-dimensional array
c=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(c)
print(c.ndim)

#ndimn can create an array of any dimension
#ndim is used to generate dimension of an array 
e=np.array([1,2,3],ndmin=5)
print(e)
print(e.ndim)