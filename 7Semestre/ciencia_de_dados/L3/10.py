import pandas as pd

tamanho_bloco = 10
reader = pd.read_csv('dados_sensor_gigante.csv', 
                     chunksize=tamanho_bloco, 
                     na_values=['NA', '-'])

print(f"{'BLOCO':<10} | {'MÉDIA TEMP':<12} | {'VALORES AUSENTES (TEMP)':<20}")
print("-" * 55)

for i, bloco in enumerate(reader, 1):
    media_temp = bloco['temperatura'].mean()
    nulos_temp = bloco['temperatura'].isna().sum()
    print(f"Bloco {i:<5} | {media_temp:<12.2f} | {nulos_temp:<20}")

print("-" * 55)