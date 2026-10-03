#Scatter Plot
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

from pandas.core import frame

plt.style.use('seaborn-v0_8-whitegrid')

date_strings=['2023-01-15', '2023-02-15', '2023-03-15', '2023-04-15', '2023-05-15', '2023-06-15']
# print(plt.style.available)dates_strings = ['2023-01-15', '2023-02-15', '2023-03-15', '2023-04-15', '2023-05-15', '2023-06-15']
salaries = [55000, 56000, 58500, 59000, 62000, 65000]
dates=[datetime.strptime(d, '%Y-%m-%d') for d in date_strings]

fig,ax=plt.subplots()
ax.scatter(dates,salaries,color='lightblue',marker='.',edgecolor='black',s=50)
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax.set_title("Employee Salary growth over time")
ax.set_xlabel("Date",fontsize=14)
ax.set_ylabel("Salary",fontsize=14)
fig.autofmt_xdate()
ax.legend(loc='upper left',frameon=False)
plt.tight_layout(pad=0.5)
plt.show()