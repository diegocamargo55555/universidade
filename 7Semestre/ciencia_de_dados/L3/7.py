import pandas as pd

df = pd.read_csv('experimento.csv', sep=';')
print(df.head())


print(df.tail())
print(df.describe())