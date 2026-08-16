#Pie Chart
from tracemalloc import start
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')
slices = ['A', 'B', 'C', 'D', 'E']
v = [10, 20, 30, 40, 50]
colors = ['lightblue','lightgreen','lightcoral','lightsalmon','lightskyblue']
explode = (0.1, 0.1, 0, 0, 0)
plt.pie(v, labels=slices, colors=colors, explode=explode, autopct='%1.1f%%',startangle=90)
plt.title("Pie Chart")
plt.show()