#Bar Chart
from matplotlib import pyplot as plt
import numpy as np
from Pandas import data
width=0.35
Dept_Salary=data.groupby('Department')[['Salary','Bonus']].mean()
x = np.arange(len(Dept_Salary.index))
plt.style.use('fivethirtyeight')
colors=['lightblue','lightgreen','lightcoral','lightsalmon','lightskyblue']
plt.bar(
    x - width/2,
    Dept_Salary['Salary'],
    width=width,
    label='Salary',
    color='lightblue'
)

plt.bar(
    x + width/2,
    Dept_Salary['Bonus'],
    width=width,
    label='Bonus',
    color='lightgreen'
)
plt.xticks(x, Dept_Salary.index)
plt.title("Salary Count by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.tight_layout()
print(Dept_Salary)
plt.ticklabel_format(style='plain', axis='y')
plt.legend()
plt.show()