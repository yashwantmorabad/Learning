#line plots
from matplotlib import pyplot as plt
import pandas as pd
from Pandas import data
import numpy as np

yearly_count = data["Join_Date"].dt.year.value_counts().sort_index()
plt.style.use('fivethirtyeight')
plt.plot(yearly_count.index, yearly_count.values)

plt.title("Salary by Year")
plt.xlabel("Year")
plt.ylabel("Salary")
plt.grid(True)
plt.tight_layout()
plt.show()