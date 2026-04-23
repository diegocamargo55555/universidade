import pandas as pd
import requests
from sqlalchemy import create_engine

# 1. Leitura de CSV Avançada
df_csv = pd.read_csv('vendas.csv', header=None, index_col=0, na_values='ND')

# 2. Manipulação de Excel
# Parte 1: Salvar DataFrame
relatorio_anual = pd.DataFrame({'Exemplo': [1, 2, 3]})
relatorio_anual.to_excel('relatorio.xlsx', sheet_name='Resultados', index=False)
df_excel_bruto = pd.read_excel('relatorio.xlsx', sheet_name='Dados Brutos')

# 3. Consumindo APIs Web
url = 'https://api.dados.exemplo/usuarios'
response = requests.get(url)
dados_json = response.json()
df_usuarios = pd.DataFrame(dados_json)

# 4. Conexão com Banco de Dados
engine = create_engine('sqlite:///meu_banco.db')
query = "SELECT * FROM produtos"
df_produtos = pd.read_sql(query, engine)