import pandas as pd

df = pd.read_csv(
    'log_sistema.csv',
    comment='#',        
    nrows=2,            
    engine='python'     
    )
print("Conteúdo do seu DataFrame:")
print(df)