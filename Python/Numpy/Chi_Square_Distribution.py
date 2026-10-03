"df is degree of freedom"
from numpy import random
a=random.chisquare(df=1,size=1000)
print(a)
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(a,kind="kde")
plt.show()