#Bar Chart
from turtle import color
from matplotlib import pyplot as plt
import pandas as pd
from Pandas import data

employee_count=data.groupby('Department')['Employee_ID'].count()
plt.style.use('fivethirtyeight')
colors=['lightblue','lightgreen','lightcoral','lightsalmon','lightskyblue']
plt.bar(employee_count.index, employee_count.values,color=colors)
plt.title("Employee Count by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.tight_layout()
plt.show()