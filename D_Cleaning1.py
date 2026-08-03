import pandas as pd
from numpy import mean  
df = pd.read_csv("Demo1.csv")
df = df.rename(columns={'Performance_Rating': 'Rating', 'Remote_Work': 'Remote'})
df['Salary'] = df['Salary'].str.replace('$', '')
df['Salary'] = df['Salary'].str.replace(',', '')
df['Salary'] = df['Salary'].str.strip()
df['Salary'] = df['Salary'].astype(float)

mean_age=int(mean(df['Age']))
print(mean_age)
df['Age']=df['Age'].fillna(mean_age)
df['Age'] = df['Age'].astype(int)
df['Join_Date'] = df['Join_Date'].fillna(pd.Timestamp('2022-01-01'))
df['Join_Date'] = pd.to_datetime(df['Join_Date'],format='mixed',errors='coerce')
df['Remote']=df['Remote'].map({True:'Yes',False:'No'})
print(df)