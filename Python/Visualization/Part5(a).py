import matplotlib.pyplot as plt
import numpy as np  # <--- ADD THIS IMPORT

# 1. Apply global style
plt.style.use('fivethirtyeight')

# 2. Sample Data (Ages vs Salary) - Convert lists to numpy arrays
ages_x = np.array([25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35])
all_dev_y = np.array([45372, 68876, 53850, 57287, 63016, 65998, 70003, 70007, 71596, 75370, 83640])
py_dev_y = np.array([55372, 59876, 63850, 65287, 71016, 75998, 81003, 85007, 86596, 95370, 102640])

# 3. Create Figure and Axes
fig, ax = plt.subplots()

# 4. Plot the lines FIRST (so they sit on top of the fill)
ax.plot(ages_x, py_dev_y, color='#5a7d9a', linewidth=3, label='Python Devs')
ax.plot(ages_x, all_dev_y, color='#444444', linestyle='--', linewidth=3, label='All Devs')

# 5. Conditional Fill Between (Green where Python > All)
ax.fill_between(
    ages_x, 
    py_dev_y, 
    all_dev_y, 
    where=(py_dev_y > all_dev_y),
    interpolate=True, 
    color='green', 
    alpha=0.25, 
    label='Above Overall Average'
)

# 6. Conditional Fill Between (Red where Python < All)
ax.fill_between(
    ages_x, 
    py_dev_y, 
    all_dev_y, 
    where=(py_dev_y <= all_dev_y), 
    interpolate=True, 
    color='red', 
    alpha=0.25, 
    label='Below Overall Average'
)

# 7. Format the Axes
ax.set_title('Median Salary (USD) by Age', fontsize=14)
ax.set_xlabel('Ages', fontsize=12)
ax.set_ylabel('Median Salary (USD)', fontsize=12)

# 8. Add Legend and adjust layout
ax.legend(loc='upper left', frameon=False)
plt.tight_layout(pad=1.5)

# 9. Show plot
plt.show()