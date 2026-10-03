import matplotlib.pyplot as plt
import numpy as np
from Pandas import data
import pandas as pd

plt.style.use('fivethirtyeight')
data['Join_Date']=pd.to_datetime(data['Join_Date'],errors='coerce')
data['Year']=data['Join_Date'].dt.year

data['Year'] = data['Join_Date'].dt.year

employee_count = (
    data.groupby(['Year', 'Department'])['Employee_ID']
        .count()
        .unstack(fill_value=0)
)

# print(employee_count)
       
plt.stackplot(
    employee_count.index,
    *[employee_count[col] for col in employee_count.columns],
    labels=employee_count.columns
)
plt.legend()
plt.title("Salary by Department")
plt.tight_layout()
plt.show()