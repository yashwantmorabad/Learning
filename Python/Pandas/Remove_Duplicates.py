import pandas as pd
from numpy import mean
data = pd.read_csv("Demo1.csv")
mean_age=int(mean(data['Age']))
print(mean_age)
data['Age']=data['Age'].fillna(mean_age)
print(data)
#Find the duplicate rows
dups = data['Age'].duplicated()
print(dups)
data = data.drop_duplicates(subset=['Age'])
print(data)