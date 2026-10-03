import numpy as np
from numpy import random
print(random.randint(10))
print(random.rand(1))
print(random.rand(2))
print(random.rand(3))

"Array of random values"
a=random.randint(100,size=(5))
print(a)
b=random.randint(100,size=(3,5))
print(b)
"For float use rand only"

"choice()"
c=random.choice([1,2,3,4,5,6,7,8,9,10])
print(c)

d=random.choice([1,2,3,4,5,6,7,8,9,10],size=(2))
print(d)

e=random.choice([1,2,3,4,5,6,7,8,9,10],size=(2,3))
print(e)

