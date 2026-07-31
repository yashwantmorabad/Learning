import pandas as pd
df=pd.read_csv("Demo.csv",na_values=["NA","NULL"])
print(df)
df.to_csv("Demo1.csv",index=False)
print(pd.read_csv("Demo1.csv"))
'''Here there is no difference between two csv file 
because we have not changed the data in the csv file'''