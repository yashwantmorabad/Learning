#Scatter Plot
import matplotlib.pyplot as plt
from Pandas import data

plt.style.use('seaborn-v0_8-whitegrid')
color=data['Performance_Rating']
fig,ax=plt.subplots()
scatter=ax.scatter(data['Salary'],data['Performance_Rating'],
cmap='Greens',linewidth=0.5,c=color,
marker='.',edgecolor='black',s=100) 
cbar=plt.colorbar(scatter,ax=ax)
cbar.set_label("Performance Rating")
ax.set_title("Scatter Plot")
ax.set_xlabel("Salary")
ax.set_ylabel("Performance Rating")
fig.savefig("C:/Users/VICTUS/GitHub/Visualization/Part7(a).png")
plt.tight_layout()
plt.show()