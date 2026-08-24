import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

ages_x=[25,26,27,28,29,30,31,32,33,34,35]
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70007, 71596, 75370, 83640]
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

fig,(ax1,ax2)=plt.subplots(nrows=2,ncols=1,figsize=(10,10))
# ax.plot(ages_x,py_dev_y,linestyle='-',marker='.',linewidth=2,label="Python")
# ax.plot(ages_x,js_dev_y,linestyle='--',marker='.',linewidth=2,label="JavaScript")

# ax.set_title("Median Salaries by Age")
# ax.set_xlabel("Age",fontsize=14)
# ax.set_ylabel("Salary",fontsize=14)
# ax.legend(loc='best')
# plt.tight_layout()
# fig.savefig("C:/Users/VICTUS/GitHub/Visualization/Part1(b).png")

ax1.plot(ages_x,py_dev_y,linestyle='-',marker='.',linewidth=2,label="Python")
ax2.plot(ages_x,js_dev_y,linestyle='--',marker='.',linewidth=2,label="JavaScript")
ax1.set_title("Median Salaries by Age of Python Devs")
ax2.set_title("Median Salaries by Age of JavaScript Devs")
plt.tight_layout()
ax1.legend(loc='best')
plt.show()
