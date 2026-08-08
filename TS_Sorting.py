import pandas as pd
def clean_data(df):
    df = df.copy()

    df['Salary'] = (
        df['Salary']
        .str.replace('$', '', regex=False)
        .str.replace(',', '', regex=False)
        .astype(float)
    )

    df['Age'] = df['Age'].fillna(df['Age'].mean()).astype(int)

    df['Join_Date'] = pd.to_datetime(
        df['Join_Date'],
        format='mixed',
        errors='coerce'
    )

    df['Performance_Rating'] = (
        df['Performance_Rating']
        .fillna(df['Performance_Rating'].mean())
    )

    df['Join_Date'] = df['Join_Date'].fillna(pd.Timestamp('2022-01-01'))

    return df

df = pd.read_csv('Demo1.csv')
data1=clean_data(df)

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
new_employees_df = pd.DataFrame(new_hires_data)
data2=clean_data(new_employees_df)
combined_df = pd.concat([data1, data2], ignore_index=True)
# print(combined_df)

#Time Series
combined_df['Date']=pd.to_datetime(combined_df['Join_Date'])
print(combined_df['Date'])

#.dt accessor
print(combined_df['Date'].dt.year)
print(combined_df['Date'].dt.month)
print(combined_df['Date'].dt.day)

#Ranking the employees by salary
salary_rank=combined_df['Salary'].rank(method='first',ascending=False)
salary_rank_df=pd.DataFrame({
    'Name':combined_df['Name'],
    'Salary':combined_df['Salary'],
    'Salary_Rank':salary_rank
}).sort_values(by='Salary_Rank')
print(salary_rank_df)

#Functions to find max and min 
top_3=combined_df.nlargest(3,'Salary')
print(top_3)
youngest_3=combined_df.nsmallest(3,'Age')
print(youngest_3)