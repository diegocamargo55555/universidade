import pandas as pd

df = pd.read_csv('notas.csv', sep=';')
print(df.describe())

#8.5,   7.0,    9.0