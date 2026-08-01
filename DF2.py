import pandas as pd
# 1. Read the CSV file
df = pd.read_csv("Demo1.csv")

# 2. Convert and save it to an Excel file
df.to_excel("Demo1.xlsx", index=False, engine='openpyxl')
print(pd.read_excel("Demo1.xlsx"))

