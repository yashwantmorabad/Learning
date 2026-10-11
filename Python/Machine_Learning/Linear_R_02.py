# import numpy as np
# import matplotlib.pyplot as plt

# x=np.array([1,2,3,4,5])
# y=np.array([2,3,5,4,6])

# mean_y=np.mean(y)

# tota_variation=np.sum((y-mean_y)**2)

# slope, intercept=np.polyfit(x,y,deg=1)
# predicted_y=slope*x+intercept
# regression_variation=np.sum((predicted_y-y)**2)
# r_squared=(tota_variation-regression_variation)/tota_variation

# #print all
# print(f"R^2 = {r_squared:.4f}")
# print(f"Total variation = {tota_variation:.4f}")
# print(f"Regression variation = {regression_variation:.4f}")
# print(f"Slope = {slope:.4f}")
# print(f"Intercept = {intercept:.4f}")
# print(f"Predicted y = {predicted_y}")
# print(f"Conclusion: The regression line is {r_squared * 100:.1f}% better than just guessing the average!")

#F-test for the slope
import statsmodels.api as sm
import numpy as np

# 1. The Data
x = np.array([1, 2, 3, 4, 5]) 
y = np.array([2, 3, 5, 4, 6])

# 2. Add a constant (Statsmodels requires this to calculate the intercept)
x_with_constant = sm.add_constant(x)

# 3. Fit the model and print the summary!
model = sm.OLS(y, x_with_constant).fit()
print(model.summary())
"""
1. Top Right: The "Overall Model" Grade
This section looks at the big picture and tells you if your entire regression line is actually useful.
R-squared: This should say 0.820. This is the exact percentage we calculated earlier! It means your slanted line explains 82% of the variation in the data.
F-statistic: This should say 13.67. This is the signal-to-noise ratio (the formula we just discussed). The signal is over 13 times stronger than the noise.
Prob (F-statistic): This is the overall p-value for the model. It should say 0.0343. Because 0.0343 is less than our magic threshold of 0.05, it mathematically proves your line is statistically significant and not just a lucky fluke.

2. The Middle Table: The Variables
This table builds your actual mathematical equation and grades your specific inputs.
const (The Intercept):
Look at the coef (coefficient) column. It says 1.3000. This is your starting point—where the line crosses the Y-axis.
x1 (Your Input Variable / The Slope):
Look at the coef column. It says 0.9000. This is your slope! For every 1 unit of X (weight), Y (size) goes up by 0.9.
Look at the P>|t| column. This is the p-value for just this specific variable. It also says 0.034. Because it is under 0.05, X is a significant predictor of Y.
"""