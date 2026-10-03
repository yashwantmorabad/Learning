import pandas as pd
df=pd.read_csv("Demo.csv")
print(df)
print(df.head(5))
print(df.tail(5))
print(df.info())
print(df["Salary"].max())
print(df["Age"].max())
print(df.describe())#Use to find statistics of the data
print(df["Age"]>30)
# Get list of names in one line
names_list = df[df['Age'] > 30]['Name'].tolist()

# 1. Filter the DataFrame to only keep rows where Age is greater than 30
filtered_df = df[df['Age'] > 30]

# 2. Extract the 'Name' column and convert it to a Python list using .tolist()
names_list = filtered_df['Name'].tolist()

# 3. Do the same for 'Employee_ID'
ids_list = filtered_df['Employee_ID'].tolist()

print("People older than 30 (Names):", names_list)
print("People older than 30 (IDs):", ids_list)

print(df.index)
print(df.set_index("Age"))
df.set_index("Age",inplace=True)
print(df)
print(df.loc[29.0])
df.reset_index(inplace=True)
print(df)
print(df[['Name','Age']])
# Get row at index 0, and column 'Name'
print(df.loc[0, 'Name']) 
print(df.iloc[0, 0])