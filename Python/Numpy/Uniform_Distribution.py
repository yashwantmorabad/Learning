"Uniform Disribution-It is made for probability(p)"
'Parameters-upper bound(a),lower bound(b),size(n)'
from numpy import random
from seaborn.external import kde
a=random.uniform(size=(1000))
print(a)

#Visualisation
import matplotlib.pyplot as plt
import seaborn as sns
# sns.displot(a,kind="kde")
# plt.show()

arrival_times =random.uniform(low=1.0, high=1.5, size=50)
print(arrival_times)
sns.displot(arrival_times,kde=True)
plt.show()