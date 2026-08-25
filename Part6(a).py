import matplotlib.pyplot as plt


plt.style.use('fivethirtyeight')
ages=[22, 25, 26, 27, 28, 29, 30, 31,
 32, 33, 35, 36, 38, 40, 45]

fig,ax=plt.subplots()
ax.hist(
    ages,
    bins=[20,25,30,35,40,45,50],
    color='lightblue',
    edgecolor='black',
    alpha=0.5
)

ax.set_title("Age Distribution")
ax.set_xlabel("Age")
ax.set_ylabel("Count")
ax.set_xlim(15,55)
ax.set_ylim(0,6)
plt.tight_layout(pad=0.5)
plt.show()