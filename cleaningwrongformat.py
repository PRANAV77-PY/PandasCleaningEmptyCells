import pandas as pd

df = pd.read_csv('D:\Software engg Professional training\Python Basics\Python Pandas\pandas clean data\Book1.csv')

df['Date'] = pd.to_datetime(df['Date'],format = 'mixed')

df.dropna(subset = ['Date'],inplace =True)

print(df.to_string())