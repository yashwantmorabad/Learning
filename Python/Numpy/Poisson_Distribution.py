"PD-It estimates how many times an event can happen."
from numpy import random
a=random.poisson(lam=2,size=10)
b=random.normal(loc=1,scale=2,size=(2,3))
print(a)
print(b)

#Visualisation
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(a,discrete=True,shrink=0.8,kde=False)
sns.displot(b,kde=False)
plt.show()