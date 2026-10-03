import pandas as pd
import numpy as np

df=pd.read_csv('employee_visualization_data.csv')
# print(df.dtypes)
# print(df.isnull().sum())
def clean_data(df):
    df['Join_Date']=pd.to_datetime(df['Join_Date'],errors='coerce')
    df.fillna({
        'Bonus':df['Bonus'].mean(),
        'City':"Unknown",},inplace=True)
    df['Performance_Rating']=df['Performance_Rating'].interpolate()
    return df

data=clean_data(df)
department_counts = df.groupby('Department')['Employee_ID'].count()
# print(department_counts)
