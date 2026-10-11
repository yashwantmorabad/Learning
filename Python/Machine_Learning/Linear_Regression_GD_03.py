import numpy as np

x=np.array([1,2,3,4,5])
y=np.array([2,3,5,4,6])
n=len(x)

#Least squares
ls_slope,ls_intercept=np.polyfit(x,y,deg=1)

print("Least Squares")
print(f"Slope = {ls_slope:.4f}")
print(f"Intercept = {ls_intercept:.4f}")

#Gradient Descent
m=0.0 #slope
c=0.0 #intercept

learning_rate=0.01
epochs=1000

for i in range(epochs):
    y_pred=m*x+c

    derivative_m=(-2/n)*sum(x*(y-y_pred))#derivative with respect to slope
    derivative_c=(-2/n)*sum(y-y_pred)#derivative with respect to intercept

    m=m-learning_rate*derivative_m
    c=c-learning_rate*derivative_c
    
print("Gradient Descent")
print(f"Slope = {m:.4f}")
print(f"Intercept = {c:.4f}")

#sklearn
from sklearn.linear_model import LinearRegression

# 1. Initialize the model
model = LinearRegression()

# 2. Fit the model (Scikit-Learn expects 2D data for X, so we reshape it)
model.fit(x.reshape(-1, 1), y)

# 3. Print the results
print(f"Scikit-Learn Slope: {model.coef_[0]:.4f}")
print(f"Scikit-Learn Intercept: {model.intercept_:.4f}")