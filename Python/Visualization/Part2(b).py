#Bar Chart
from matplotlib import pyplot as plt
import pandas as pd
from Pandas import data

employee_count=data.groupby('Department')['Employee_ID'].count()
plt.style.use('fivethirtyeight')
colors=['lightblue','lightgreen','lightcoral','lightsalmon','lightskyblue']

employee_count=employee_count.sort_values(ascending=True)

plt.barh(employee_count.index, employee_count.values,color=colors)
plt.title("Employee Count by Department")
plt.ylabel("Department")
plt.xlabel("Count")
plt.tight_layout()
plt.show()