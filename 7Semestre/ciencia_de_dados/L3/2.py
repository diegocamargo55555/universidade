import pandas as pd

df = pd.read_csv(
    'clima.csv',
    parse_dates=['data'],  
    index_col='data'     
)

print("info:")
df.info()

print("\n")
print(df)