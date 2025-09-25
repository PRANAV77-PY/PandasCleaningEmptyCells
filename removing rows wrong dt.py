import pandas as pd

df = pd.read_csv('D:\Software engg Professional training\Python Basics\Python Pandas\pandas clean data\Book1.csv')

for x in df.index:
    if df.loc[x,"Duration"] > 120:
        df.drop(x,inplace = True)

print(df.to_string())