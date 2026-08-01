from numpy import mean
import pandas as pd
df = pd.read_csv("Demo1.csv")
missing_age=df['Age'].isnull()
print(df.loc[missing_age])
print(missing_age)
mean_age=int(mean(df['Age']))
print(mean_age)
df['Age']=df['Age'].fillna(mean_age)
print(df)
df['Age']=df['Age'].fillna(df['Age'].mean()).astype(int)
print(df)       