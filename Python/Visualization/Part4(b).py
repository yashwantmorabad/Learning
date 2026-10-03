import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

days = [1, 2, 3, 4, 5]  

coding_min = [180, 150, 200, 210, 160]      
meetings_min = [60, 90, 70, 50, 80]          
admin_min = [30, 40, 20, 60, 30]             

colors = ['#008fd5', '#fc4f30', '#e5ae38']  # Blue, Red, Yellow
labels = ['Coding', 'Meetings', 'Admin']

fig, ax = plt.subplots()
ax.stackplot(
    days, 
    coding_min, 
    meetings_min, 
    admin_min, 
    labels=labels,
    colors=colors,
    alpha=0.75  # Transparency
)

ax.set_title('Daily Time Distribution Over a Work Week', fontsize=14)
ax.set_xlabel('Day of Week')
ax.set_ylabel('Minutes Spent')
ax.legend(loc='upper left', frameon=False)

plt.tight_layout(pad=2.0)
plt.show()