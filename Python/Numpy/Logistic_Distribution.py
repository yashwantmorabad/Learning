"Logistic Distribution-It describes the growth"
'Parameters-loc(mean-0),scale(SD),size(n)'
from numpy import random
a=random.logistic(loc=1,scale=2,size=(2,3))
print(a)
b=random.logistic(loc=1,scale=1,size=1000)
print(b)

#Visualisation
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(b,kind="kde")
plt.show()