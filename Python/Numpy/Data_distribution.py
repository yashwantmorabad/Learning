"1-D array with 100 values where each value is 3,5,7,9"
'The probablity of 3 is 0.1'
'The probablity of 5 is 0.2'
'The probablity of 7 is 0.3'
'The probablity of 9 is 0.4'
from numpy import random
a=random.choice([3,5,7,9],p=[0.1,0.2,0.3,0.4],size=(100))
print(a)
import numpy as np
# 2. Get unique elements and their counts
elements, counts = np.unique(a, return_counts=True)

# 3. Print the results clearly
for element, count in zip(elements, counts):
    print(f"Element {element} appears {count} times")

"2-D array with 3 rows and each contains 5 vslues"
from numpy import random
b=random.choice([3,5,7,9],p=[0.1,0.2,0.3,0.4],size=(3,5))
print(b)
ele, cou = np.unique(b,axis=0,return_counts=True)
for elem, coun in zip(ele, cou):
    print(f"Element {elem} appears {coun} times")
    
"Note:If axis=0 is there then output will be the number of that particular row appeears"
'''Note:If axis=0 is not there the output is that how many times that particular number
is there in list '''