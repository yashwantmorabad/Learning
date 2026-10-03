#Scatter Plot
import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9,10]
y=[1,2,3,4,5,6,7,8,9,10]

fig,ax=plt.subplots()
ax.scatter(x,y,color='lightblue',marker='.',edgecolor='black',s=50) 
ax.set_title("Scatter Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
# ax.set_xlim(0,11)
# ax.set_ylim(0,11)
plt.tight_layout()
plt.show()