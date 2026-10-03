import numpy as np
arr = np.array([1, 2, 3])
result = arr + 10  # 10 is broadcasted across the array
print(result)

matrix = np.ones((3, 3))
vector = np.array([1, 2, 3])
print(matrix)
# The vector [1, 2, 3] is added to every single row
res = matrix + vector
print(res)