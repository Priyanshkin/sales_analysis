import pandas as pd
print("hello pandas")
df=pd.read_csv("salesdata.csv")
df.to_excel("salesdata.xlsx",index=False)
excel_data=pd.read_excel("salesdata.xlsx")
print(excel_data.head(5))