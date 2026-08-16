#Pie Chart
from matplotlib import pyplot as plt
from Pandas import data

plt.style.use('fivethirtyeight')

dept=data.groupby('Department')['Employee_ID'].count()  

def show_value(pct):
    total=dept.sum()
    value=int(round(pct * total / 100))
    return f'{value}'
plt.pie(dept.values,labels=dept.index,autopct=show_value,startangle=90) 

plt.title("Employee Count by Department")
plt.show()