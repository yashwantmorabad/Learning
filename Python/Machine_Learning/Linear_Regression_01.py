# For linear regression we need to find the fitting line
# that best fits the data points.

import numpy as np
import matplotlib.pyplot as plt

x=np.array([0.5,2.3,2.9])
y=np.array([1.4,1.9,3.2])

#ssr is the sum of the squared residuals
def ssr(a,b):
    y_hat=a*x+b
    residuals=y-y_hat
    return np.sum(residuals**2)

# Closed form solution
X_mean,y_mean=x.mean(),y.mean()
a=np.sum((x-X_mean)*(y-y_mean))/np.sum((x-X_mean)**2) # slope
b=y_mean-a*X_mean # intercept
print(f"Closed form -> slope = {a:.4f}, intercept = {b:.4f}, SSR = {ssr(a,b):.4f}")

# Brute force search
best=(None,None,np.inf)
for cand_a in np.linspace(-2,3,501): 
    for cand_b in np.linspace(-1,3,401):
        s=ssr(cand_a,cand_b)
        if s<best[2]:
            best=(cand_a,cand_b,s)
print(f"Brute force  -> slope = {best[1]:.4f}, intercept = {best[0]:.4f}, SSR = {best[2]:.4f}")

np_b,np_a=np.polyfit(x,y,deg=1)
print(f"Numpy polyfit -> slope = {np_a:.4f}, intercept = {np_b:.4f},")

fig,(ax1,ax2)=plt.subplots(1,2,figsize=(12,4.5))
xs=np.linspace(0,3.2,100)
ax1.scatter(x,y,color="black", zorder=3, label="data points")
ax1.plot(xs,a*xs+b,color="red",zorder=2, 
label="best fit line: y = {a:.2f} + {b:.2f}x")
for xi,yi in zip(x,y):
    ax1.plot([xi,xi],[yi,a*xi+b],color="tab:green",linestyle="--") #residual

ax1.set_xlabel("x") 
ax1.set_ylabel("y")
ax1.set_title("Least Squares Fit")
ax1.legend(loc="upper left")

#ssr as a function of a and b
slopes=np.linspace(-1,3,200)
ax2.plot(slopes,[ssr(s,b) for s in slopes])
ax2.scatter([b], [ssr(a, b)], color="tab:red", zorder=3, label="minimum SSR")
ax2.set_xlabel("Slope")
ax2.set_ylabel("SSR")
ax2.set_title("SSR vs slope (intercept fixed)")
ax2.legend()
 
plt.tight_layout()
plt.savefig("E:\Projects\Learning\Python\Machine_Learning\Linear_Regression_01.png")
plt.show()