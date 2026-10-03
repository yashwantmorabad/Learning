from turtle import width
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')
lang=['JavaScript', 'HTML/CSS', 'Python', 'SQL', 'TypeScript']
ages=np.arange(len(lang))

dev_y = [59219, 55465, 47544, 36443, 33342]      # All developers
py_dev_y = [57565, 45342, 30000, 25000, 28000]  # Python developers

width=0.25
fig,ax=plt.subplots()
ax.bar(ages-width/2,dev_y,width=width,edgecolor='black',label='All Devs',color='lightblue')
ax.bar(ages+width/2,py_dev_y,width=width,edgecolor='black',label='Python Devs',color='lightgreen')
ax.set_xticks(ages)
ax.set_xticklabels(lang)
ax.set_title("Salary Count by Language")
ax.set_xlabel("Language")
ax.set_ylabel("Salary")
plt.legend()
plt.show()