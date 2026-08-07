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
print(combined_df)

# Resahping the data
# 1. Melt: Turn Age and Salary into a single "Metric" column
df_melted = combined_df.melt(id_vars=['Employee_ID', 'Name'], 
                    value_vars=['Age', 'Salary'],
                    var_name='Metric', 
                    value_name='Amount')
print(df_melted)
# 2. Unstack: Move the Department groupby index to columns
df_grouped = combined_df.groupby(['City', 'Department'])['Salary'].mean()
print(df_grouped)
df_unstacked = df_grouped.unstack() # Departments become columns
print(df_unstacked)
# 3. Transpose
combined_df.head(3).T
print(combined_df.head(3).T)
