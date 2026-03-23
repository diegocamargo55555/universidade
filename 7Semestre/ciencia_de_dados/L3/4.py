import pandas as pd

df = pd.read_csv(
    'estoque.csv',
    sep=';',
    decimal=',', 
    dtype={
        'valor_unitario': 'float64',
        'peso_kg': 'float64'
    }
)
print("Tipos de dados (.dtypes):")
print(df.dtypes)

print("\nConteúdo do DataFrame:")
print(df)