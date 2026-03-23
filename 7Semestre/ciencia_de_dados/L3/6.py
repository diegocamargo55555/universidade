import pandas as pd
df =df = pd.read_csv(
    'sensores.csv',
    sep=';',
    na_values=['-', 'NA', 'null']
)

print(df)
df.info()


