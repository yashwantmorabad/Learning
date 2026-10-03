'''Exponential Disttribution-Used for describing the time till
next event occurs'''

from numpy import random
a=random.exponential(scale=2,size=(1000))
print(a)
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(a,kind="kde")
plt.show()