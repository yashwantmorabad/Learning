import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5])
y=np.array([2,3,5,4,6])

mean_y=np.mean(y)

tota_variation=np.sum((y-mean_y)**2)

slope, intercept=np.polyfit(x,y,deg=1)
predicted_y=slope*x+intercept
regression_variation=np.sum((predicted_y-y)**2)
r_squared=(tota_variation-regression_variation)/tota_variation

#print all
print(f"R^2 = {r_squared:.4f}")
print(f"Total variation = {tota_variation:.4f}")
print(f"Regression variation = {regression_variation:.4f}")
print(f"Slope = {slope:.4f}")
print(f"Intercept = {intercept:.4f}")
print(f"Predicted y = {predicted_y}")
print(f"Conclusion: The regression line is {r_squared * 100:.1f}% better than just guessing the average!")