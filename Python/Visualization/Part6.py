#Histogram
import matplotlib.pyplot as plt
from Pandas import data

plt.style.use('fivethirtyeight')
bins=[2,3,4,5]
fig,(ax1,ax2)=plt.subplots(nrows=2,ncols=1,figsize=(10,10))
ax1.hist(data['Performance_Rating'],
bins=bins,color='lightblue',edgecolor='black')
ax1.set_title("Performance Rating Distribution") 
ax1.set_xlabel("Performance Rating")
ax1.set_ylabel("Count")
bins2=[20000,40000,60000,80000,100000,120000,140000,160000,180000]
ax2.hist(data['Salary'],bins=bins2,
edgecolor='black',color='lightblue')
ax2.set_title("Salary Distribution")
ax2.set_xlabel("Salary")
ax2.set_ylabel("Count")
plt.tight_layout()
print(data['Performance_Rating'])
# print(data.loc[data['Salary'].between(100000,200000),"Salary"])

plt.tight_layout()
plt.legend(loc='best')
plt.show()