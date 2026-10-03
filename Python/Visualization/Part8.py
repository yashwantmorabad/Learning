import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# 1. Apply global style
plt.style.use('seaborn-v0_8-whitegrid') # A nice clean style for time series

# 2. Sample Data (Dates as strings, and Salaries)
dates_strings = ['2023-01-15', '2023-02-15', '2023-03-15', '2023-04-15', '2023-05-15', '2023-06-15']
salaries = [55000, 56000, 58500, 59000, 62000, 65000]

# 3. Convert date strings to datetime objects
# This is the most important step for Matplotlib to understand the time scale
dates = [datetime.strptime(d, '%Y-%m-%d') for d in dates_strings]

# 4. Create Figure and Axes
fig, ax = plt.subplots()

# 5. Plot the Time Series Data
ax.plot(dates, salaries, color='#008fd5', marker='o', linewidth=2, label='Salary')

# 6. Format the X-Axis using mdates
# Tell Matplotlib to put a tick at the start of every month
ax.xaxis.set_major_locator(mdates.MonthLocator())

# Tell Matplotlib to format those ticks as "Month Year" (e.g., "Jan 2023")
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

# 7. Format the Axes
ax.set_title('Employee Salary Growth Over Time', fontsize=14)
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Salary (USD)', fontsize=12)

# 8. Rotate the dates automatically so they don't overlap
fig.autofmt_xdate()

# 9. Add Legend and adjust layout
ax.legend(loc='upper left', frameon=False)
plt.tight_layout(pad=1.5)

# 10. Show plot
plt.show()