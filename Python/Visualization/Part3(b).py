#Pie Chart
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')
departments = ['Engineering', 'Sales', 'HR', 'Marketing', 'Support']
employee_counts = [15, 20, 20, 15, 30]
explode=(0.1, 0, 0, 0, 0)
fig,ax=plt.subplots()
ax.pie(
    employee_counts,
    labels=departments,
    colors=['lightblue','lightgreen','lightcoral','lightsalmon','lightskyblue'],
    explode=explode,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'linewidth':1.5,'edgecolor':'black'}
    )

ax.set_title("Employee Count by Department")
plt.show()