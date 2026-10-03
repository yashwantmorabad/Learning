from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
# a=random.rayleigh(scale=2,size=1000)
# print(a)
# sns.displot(a,kind="kde")
# plt.show()

"Both Chi-square and Rayleigh Distribution"
r=random.rayleigh(scale=2,size=1000)
c=random.chisquare(df=2,size=1000)
print(r)
print(c)
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
# Plot Rayleigh
sns.histplot(r, kde=True, color="blue", 
             label="Rayleigh (scale=1.0)", stat="density", alpha=0.4)

# Plot Chi-Square
sns.histplot(c, kde=True, color="orange", 
             label="Chi-Square (df=2)", stat="density", alpha=0.4)
plt.title("Comparison: Rayleigh vs. Chi-Square Distribution", fontsize=15)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Density", fontsize=12)
plt.legend()
plt.show()
