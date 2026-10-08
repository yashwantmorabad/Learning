#It is the visual representation of the how good the regression line is.
#Also we used same data which is used in Linear_R_02.py
import numpy as np
import matplotlib.pyplot as plt

# 1. The Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 4, 6])

# Calculate Mean and Regression parameters
mean_y = np.mean(y)
slope, intercept = np.polyfit(x, y, 1)

# 2. Setup the Dark Theme (Matching your image)
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#1e1e1e') # Dark gray background
ax.set_facecolor('#1e1e1e')

# 3. Plot the Regression Line (Green)
x_line = np.linspace(0.5, 5.5, 100)
reg_line_y = slope * x_line + intercept
ax.plot(x_line, reg_line_y, color='#2ecc71', linewidth=2, 
        label=f'Regression Line (y = {slope:.1f}x + {intercept:.1f})')

# 4. Plot the Mean Line (Horizontal Dashed)
ax.axhline(mean_y, color='#8aa4c8', linestyle='--', linewidth=2, 
           label=f'Mean Line (y = {mean_y:.1f})')

# 5. Plot the Residuals (Errors to Mean Line)
for i in range(len(x)):
    # Draw vertical dashed red line from data point to mean line
    ax.plot([x[i], x[i]], [mean_y, y[i]], color='#ff4757', linestyle='--', zorder=1)
    
    # Add text label for the residual (e.g., "+2.0" or "-1.0")
    residual = y[i] - mean_y
    if residual != 0:
        ax.text(x[i] + 0.08, mean_y + (residual / 2), f'{residual:+.1f}', 
                color='#ff4757', fontsize=11, fontstyle='italic', va='center')

# 6. Plot the Data Points (Blue Circles)
ax.scatter(x, y, color='#90caf9', s=100, edgecolor='white', linewidth=1.5, 
           zorder=2, label='Data Points')

# 7. Formatting and Labels
ax.set_title('Linear Regression Residuals\nErrors to Mean Line', fontsize=16, pad=15, loc='left')
ax.set_xlabel('Mouse Weight (g)', fontsize=12, fontweight='bold')
ax.set_ylabel('Mouse Size (cm)', fontsize=12, fontweight='bold')

# Set axis limits to match the image
ax.set_xlim(0.5, 5.5)
ax.set_ylim(0, 7)

# Faint grid lines
ax.grid(color='#333333', linestyle='-', alpha=0.5)

# Place legend at the bottom
ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.2), ncol=3, frameon=False, fontsize=11)

plt.tight_layout()
plt.savefig("E:\Projects\Learning\Python\Machine_Learning\Linear_R_02(a).png")
plt.show()