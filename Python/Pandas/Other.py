import pandas as pd
from numpy import mean
df = pd.read_csv("Demo1.csv")
df['Salary'] = df['Salary'].str.replace('$', '',regex=False)
df['Salary'] = df['Salary'].str.replace(',', '',regex=False)
df['Salary'] = df['Salary'].str.strip()
df['Salary'] = df['Salary'].astype(float)

mean_age=int(mean(df['Age']))
df['Age']=df['Age'].fillna(mean_age)
df['Age'] = df['Age'].astype(int)

df['Join_Date'] = pd.to_datetime(df['Join_Date'],format='mixed',errors='coerce')
df['Join_Date'] = df['Join_Date'].fillna(pd.Timestamp('2022-01-01'))

df['Performance_Rating']=df['Performance_Rating'].fillna(df['Performance_Rating'].mean())
# df=df.drop_duplicates(subset=['Age'])


dept_stats=df.groupby('Department').agg(Total_employees=('Employee_ID','count'),
Avg_Age=('Age','mean'))
df['Dept_Avg_Sal']=df.groupby('Department')['Salary'].transform('mean')
print(dept_stats)

# Pivot Table: Average Salary by Department (rows) and Remote_Work (columns)
print(pd.pivot_table(df, index='Department', columns='Remote_Work', values='Salary', aggfunc='sum'))

# Crosstab: How many employees in each City are Remote vs Non-Remote?
print(pd.crosstab(df['Remote_Work'],df['City']))

print(df)

#Merging and Joining
# Creating a dictionary with our 3 new employees
new_hires_data = {
    'Employee_ID': [113, 114, 115],
    'Name': ['Oscar Martinez', 'Pam Beesly', 'Jim Halpert'],
    'Department': ['IT', 'HR', 'Sales'],
    'Age': [36.0, 29.0, 31.0],
    'Salary': ["$71,000.00", "$60,000.00", "$78,500.00"],
    'Join_Date': ['2023-10-01', '2023-11-15', '2023-11-15'],
    'Performance_Rating': [None, 4.5, 4.0],  # Oscar is too new for a rating
    'Remote_Work': [False, False, False],
    'City': ['Boston', 'New York', 'Los Angeles']
}

# Convert the dictionary into a Pandas DataFrame
new_employees_df = pd.DataFrame(new_hires_data)
new_employees_df['Salary'] = new_employees_df['Salary'].str.replace('$', '')
new_employees_df['Salary'] = new_employees_df['Salary'].str.replace(',', '')
new_employees_df['Salary'] = new_employees_df['Salary'].str.strip()
new_employees_df['Salary'] = new_employees_df['Salary'].astype(float)

new_employees_df['Join_Date'] = pd.to_datetime(new_employees_df['Join_Date'],format='mixed',errors='coerce')
new_employees_df['Join_Date'] = new_employees_df['Join_Date'].fillna(pd.Timestamp('2022-01-01'))

new_employees_df['Performance_Rating']=new_employees_df['Performance_Rating'].fillna(df['Performance_Rating'].mean())

new_employees_df['Age']=new_employees_df['Age'].fillna(mean_age).astype(int)

# Gluing them together vertically
combined_df = pd.concat([df, new_employees_df], ignore_index=True)

combined_df['Dept_Avg_Sal']=combined_df.groupby('Department')['Salary'].transform('mean')
combined_dept_stats= combined_df.groupby('Department').agg(
    Total_employees=('Employee_ID', 'count'),
    Avg_Age=('Age', 'mean'))
print(combined_dept_stats)

# View the bottom of our new dataset
print(combined_df.tail())

print(pd.pivot_table(
    combined_df,
    index='Department',
    columns='Remote_Work',
    values='Salary',
    aggfunc='sum'
))

print(pd.crosstab(combined_df['Remote_Work'],combined_df['City']))
# print(combined_df)



