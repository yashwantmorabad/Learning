"Displot-Distribution plot(curve plot-histogram)"
import matplotlib.pyplot as plt
import seaborn as sns 
sns.displot([0,1,1,1,2,2,2,3,3,4,5],kde=False)
plt.show()
