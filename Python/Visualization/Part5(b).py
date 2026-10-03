from matplotlib import pyplot as plt
from numpy import median

# Median Developer Salaries by Age
age_x=[25,26,27,28,29,30,31,32,33,34,35]

dev_y=[38496,42000,46752,49320,53200,
        56000,62316,64928,67317,68748,73752]
# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(age_x, py_dev_y,color='k',linestyle='-',marker='.',linewidth=2,label="Python")
plt.plot(age_x, js_dev_y,color='brown',linestyle='--',marker='.',linewidth=2,label="JavaScript")
plt.plot(age_x, dev_y,color='lightgreen',marker='.',label="All Devs")

median=median(dev_y)
print(median)
plt.fill_between(age_x,dev_y,median,color='lightgreen',alpha=0.5)
plt.legend() # legend uesd to show the label
plt.title("Median Salaries by Age")
plt.xlabel("Age")
plt.ylabel("Salary")
# plt.legend(["All Devs", "Python"]) #other way to show the label

plt.tight_layout()# to make the plot fit the size of the window
plt.grid(True) 
plt.show()
