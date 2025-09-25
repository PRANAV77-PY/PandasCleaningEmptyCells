#small data set
import pandas as pd

df = pd.read_csv('D:\Software engg Professional training\Python Basics\Python Pandas\pandas clean data\Book1.csv')

df.loc[7,'Duration'] = 45

print(df.to_string())

#big data set
import pandas as pd

df = pd.read_csv('D:\Software engg Professional training\Python Basics\Python Pandas\pandas clean data\Book1.csv')

for x in df.index:
    if df.loc[x,'Duration'] > 120:
        df.loc[x,'Duration'] = 120

print(df.to_string())
