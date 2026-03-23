import pandas as pd
df =df = pd.read_csv(
    'transacoes.csv',
    sep=';',
    thousands='.',
    decimal=','
)

print(df)

