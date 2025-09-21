#Removes rows
import pandas as pd

df = pd.read_csv('D:\Software engg Professional training\Python Basics\Python Pandas\pandas clean data\Book1.csv')

df.dropna(inplace= True)

print(df.to_string())

#replace empty values
import pandas as pd

df = pd.read_csv('D:\Software engg Professional training\Python Basics\Python Pandas\pandas clean data\Book1.csv')

df.fillna(150,inplace = True)

print(df.to_string())

#replace only for specified column
import pandas as pd

df = pd.read_csv('D:\Software engg Professional training\Python Basics\Python Pandas\pandas clean data\Book1.csv')

df.fillna({'Calories': 170 },inplace = True)

print(df.to_string())
