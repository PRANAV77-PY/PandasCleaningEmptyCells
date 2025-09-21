#Mean Replace using Mean mode
import pandas as pd

df = pd.read_csv('D:\Software engg Professional training\Python Basics\Python Pandas\pandas clean data\Book1.csv')

x = df['Calories'].mean()

df.fillna({'Calories': x},inplace= True)

print(df.to_string())

#median
import pandas as pd

df = pd.read_csv('D:\Software engg Professional training\Python Basics\Python Pandas\pandas clean data\Book1.csv')

x = df['Calories'].median()

df.fillna({'Calories':x},inplace= True)

print(df.to_string())

#mode
import pandas as pd

df = pd.read_csv('D:\Software engg Professional training\Python Basics\Python Pandas\pandas clean data\Book1.csv')

x = df['Calories'].mode()[0]

df.fillna({'Calories': x},inplace=True)

print(df.to_string())

