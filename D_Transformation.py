import pandas as pd
df=pd.read_csv("Demo1.csv")
print(df)
df['Age_New']=df['Age']+1
print(df)