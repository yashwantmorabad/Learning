"MD-It is generalize of BD"
'Parameters-no. of outcomes(n),List of possible outcomes(pvals),size'
from numpy import random, size
import numpy as np
a=random.multinomial(n=6,pvals=[1/6]*6,size=1000)
print(a)
 #Viusualisation-it is not mandatory
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.displot(a,kind="kde")
# plt.show()