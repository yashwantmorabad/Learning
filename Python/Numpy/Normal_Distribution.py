"Guassian Distribution or Noraml Distribution"

'Random normal distribution'
from numpy import random
from seaborn.external import kde
a=random.normal(size=(2,3))
print(a)

'Random normal distribution with mean=1,SD=2'
from numpy import random
b=random.normal(loc=1,scale=2,size=(2,3))
print(b)

'Visualisation'
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 
sns.displot(random.normal(size=1000),kde=False)
plt.show()
#The curve of a normal dist is also called bell curve