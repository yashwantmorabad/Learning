#Stack Plot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   'B': [2, 4, 6, 8, 10],
                   'C': [3, 6, 9, 12, 15]})
        
# Create a stacked bar chart
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.stackplot(df.index, df['A'], df['B'], df['C'], labels=['A', 'B', 'C'])
ax.legend() 
plt.show() 