"Binomial Distribution(DB)-Discrete distribution"
'Parameters-n(number of trials),p(probabilty),size(shape or return array)'

import numpy as np
from numpy import random
a=random.binomial(n=10,p=0.5,size=1000)
print(a)
#Visualisation
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(a,kde=False)
plt.title('Binomial Distribution (n=10, p=0.5)')
plt.xlabel('Number of Successes')
plt.ylabel('Frequency')
plt.show()