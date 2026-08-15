from matplotlib import pyplot as plt
import numpy as np
from Pandas import data

Dept_Salary=data.groupby('Department')['Salary'].sum()
plt.style.use('fivethirtyeight')
colors=['lightblue','lightgreen','lightcoral','lightsalmon','lightskyblue']
plt.bar(Dept_Salary.index,Dept_Salary.values,color=colors)
plt.title("Salary Count by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.tight_layout()
print(Dept_Salary)
plt.ticklabel_format(style='plain', axis='y')
plt.show()