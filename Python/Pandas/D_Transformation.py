import pandas as pd
df=pd.read_csv("Demo1.csv")
print(df)
#Vectorized Operation
df['Age_New']=df['Age']+1
print(df)
df['Salary'] = df['Salary'].str.replace('$', '')
df['Salary'] = df['Salary'].str.replace(',', '')
df['Salary'] = df['Salary'].str.strip()
df['Salary'] = df['Salary'].astype(float)
#Map function
dept_codes={'HR':100,'IT':200,'Sales':300,'Marketing':400}
df['Dept_Code']=df['Department'].map(dept_codes)
#.apply function
df['Dept_Code']=df['Department'].apply(lambda x:dept_codes[x])
#Calcualting Bonus for each employee
def bonus(row):
    if row['Performance_Rating']>=4.0:
        return row['Salary']*1.1
    else:
        return row['Salary']*0.9
df['Bonus']=df.apply(bonus,axis=1)
df_str_upper = df.applymap(lambda x: x.upper() if isinstance(x, str) else x)
print(df_str_upper)

#cut and qcut
# 1. pd.cut(): Create custom Age Groups
# bins define the edges: 0-25, 26-35, 36-45, 46-100
age_bins = [0, 25, 35, 45, 100]
age_labels = ['Young', 'Mid-Career', 'Senior', 'Expert']
df['Age_Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)

# 2. pd.qcut(): Divide Salary into 3 equal-sized groups (Tertiles)
# q=3 means 3 quantiles. It automatically calculates the edges so ~4 employees fall in each group.
df['Salary_Tier'] = pd.qcut(df['Salary'], q=3, labels=['Low', 'Medium', 'High'])
print(df[['Name','Age','Salary','Bonus','Age_Group','Salary_Tier']])
print(df)


