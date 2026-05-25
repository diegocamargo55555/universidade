import requests
import pandas as pd
import matplotlib.pyplot as plt
import os
import json
import mysql.connector
from mysql.connector import errorcode

MYSQL_CONFIG = {
    'user': 'root',
    'password': 'YourNewStrongPassword',
    'host': 'localhost',
    'database': 'luso'
}

def setup_mysql():
    print("\nIniciando configuração do MySQL...")
    config_initial = {
        'user': MYSQL_CONFIG['user'],
        'password': MYSQL_CONFIG['password'],
        'host': MYSQL_CONFIG['host'],
    }
    
    db_name = MYSQL_CONFIG['database']
    
    try:
        cnx = mysql.connector.connect(**config_initial)
        cursor = cnx.cursor()
        
        try:
            cursor.execute(f"CREATE DATABASE {db_name} DEFAULT CHARACTER SET 'utf8mb4'")
            print(f"Banco de dados '{db_name}' criado.")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DB_CREATE_EXISTS:
                print(f"Banco de dados '{db_name}' já existe.")
            else:
                print(f"Erro ao criar banco de dados: {err.msg}")
                return False
        
        cursor.close()
        cnx.close()
        
        cnx = mysql.connector.connect(**MYSQL_CONFIG)
        cursor = cnx.cursor()
        
        table_sql = """
        CREATE TABLE IF NOT EXISTS imigrantes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            sobrenome VARCHAR(255),
            nome VARCHAR(255),
            naturalidade VARCHAR(255),
            idade INT,
            estado_civil VARCHAR(100),
            ocupacao_profissao VARCHAR(255),
            data_da_chegada VARCHAR(50),
            ano_chegada INT,
            procedencia VARCHAR(255),
            destino VARCHAR(255),
            ano_registro INT
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """
        cursor.execute(table_sql)
        
        try:
            cursor.execute("ALTER TABLE imigrantes ADD UNIQUE INDEX idx_unico (nome(100), sobrenome(100), naturalidade(100), data_da_chegada(50))")
        except mysql.connector.Error as err:
            if err.errno != errorcode.ER_DUP_KEYNAME:
                print(f"Aviso ao criar índice: {err.msg}")

        cursor.close()
        cnx.close()
        return True
    except mysql.connector.Error as err:
        print(f"Erro na configuração do MySQL: {err}")
        return False

def carga_dados_mysql(df_filtrado):
    print("Iniciando carga de dados no MySQL...")
    try:
        cnx = mysql.connector.connect(**MYSQL_CONFIG)
        cursor = cnx.cursor()
        
        insert_sql = """
        INSERT INTO imigrantes (
            sobrenome, nome, naturalidade, idade, estado_civil, 
            ocupacao_profissao, data_da_chegada, ano_chegada, 
            procedencia, destino, ano_registro
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            idade = VALUES(idade),
            estado_civil = VALUES(estado_civil),
            ocupacao_profissao = VALUES(ocupacao_profissao),
            procedencia = VALUES(procedencia),
            destino = VALUES(destino),
            ano_registro = VALUES(ano_registro);
        """

        dados = df_filtrado.to_dict(orient='records')
        cnx.start_transaction()
        
        for item in dados:
            val = lambda k: None if pd.isna(item.get(k)) or str(item.get(k)) == 'nan' else item.get(k)
            data = (
                val('SOBRENOME'), val('NOME'), val('NATURALIDADE'), val('IDADE'),
                val('ESTADO_CIVIL'), val('OCUPACAO_PROFISSAO'), val('DATA_DA_CHEGADA'),
                val('ANO_CHEGADA'), val('PROCEDENCIA'), val('DESTINO'), val('ANO_REGISTRO')
            )
            cursor.execute(insert_sql, data)

        cnx.commit()
        print(f"Carga finalizada: {len(dados)} registros processados.")
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(f"Erro na carga de dados: {err}")
        if 'cnx' in locals() and cnx.is_connected():
            cnx.rollback()

def gerar_graficos(df_filtrado, ano_inicio, ano_fim):
    print(f"Gerando visualizações para o período {ano_inicio}-{ano_fim}...")
    
    anos_validos = df_filtrado['ANO_CHEGADA'].dropna()
    if not anos_validos.empty:
        plt.figure(figsize=(12, 6))
        intervalos = range(int(ano_inicio), int(ano_fim) + 2)
        
        plt.hist(anos_validos, bins=intervalos, color='skyblue', edgecolor='black', align='left')
        plt.title(f'Número de Pessoas Chegando por Ano ({ano_inicio}-{ano_fim})')
        plt.xlabel('Ano')
        plt.ylabel('Total de Pessoas')
        plt.xticks(range(int(ano_inicio), int(ano_fim) + 1))
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        nome_arquivo_chegadas = f'chegadas_{ano_inicio}_{ano_fim}.png'
        plt.savefig(nome_arquivo_chegadas)
        print(f"Gráfico '{nome_arquivo_chegadas}' salvo.")

    idades_validas = df_filtrado[(df_filtrado['IDADE'] > 0) & (df_filtrado['IDADE'] <= 80)]['IDADE'].dropna()
    
    if not idades_validas.empty:
        plt.figure(figsize=(10, 6))
        plt.hist(idades_validas, bins=range(0, 81, 2), color='lightgreen', edgecolor='black')
        plt.title('Distribuição de Idade dos Imigrantes (0 a 80 anos)')
        plt.xlabel('Idade')
        plt.ylabel('Frequência')
        plt.xlim(0, 80)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.savefig('visualizacao_idade_0_80.png')
        print("Gráfico 'visualizacao_idade_0_80.png' salvo.")
    else:
        print("Sem dados de idade válidos para o gráfico de distribuição.")

url = 'https://www.gov.br/arquivonacional/pt-br/acesso-a-informacao/pda-mgi-2024-2026/Luso.xlsx'
caminho_xlsx = 'downloaded_file.xlsx'
caminho_csv = 'Luso.csv'
caminho_json = 'Luso_filtrado.json'

if not os.path.exists(caminho_xlsx):
    print(f"Baixando arquivo de {url}...")
    resposta = requests.get(url)
    if resposta.status_code == 200:
        with open(caminho_xlsx, 'wb') as f:
            f.write(resposta.content)
        print("Download concluído!")
    else:
        print(f"Erro no download: {resposta.status_code}")
        exit()

df = pd.read_excel(caminho_xlsx)
df.to_csv(caminho_csv, index=False)

for coluna in df.select_dtypes(include=['object']).columns:
    df[coluna] = df[coluna].astype(str).str.strip()

df['ANO_CHEGADA'] = pd.to_numeric(df['ANO_CHEGADA'], errors='coerce')
df['IDADE'] = pd.to_numeric(df['IDADE'], errors='coerce')

ano_inicio, ano_fim = 1829, 1839
df_filtrado = df[(df['ANO_CHEGADA'] >= ano_inicio) & (df['ANO_CHEGADA'] <= ano_fim)].copy()

df_filtrado.to_json(caminho_json, orient='records', indent=4, force_ascii=False)
print(f"Dados tratados e convertidos para '{caminho_json}'.")

print(f"\nRegistros encontrados entre {ano_inicio} e {ano_fim}: {len(df_filtrado)}")

estatisticas_idade = df_filtrado['IDADE'].dropna()

if not estatisticas_idade.empty:
    print(f"\nEstatísticas de Idade ({ano_inicio}-{ano_fim}):")
    print(f"  - Média: {estatisticas_idade.mean():.2f}")
    print(f"  - Máximo: {estatisticas_idade.max()}")
    print(f"  - Mínimo: {estatisticas_idade.min()}")

def analise_adicional_mysql():
    print("\ngrafico mysql")
    try:
        cnx = mysql.connector.connect(**MYSQL_CONFIG)
        
        query_nat = "SELECT naturalidade, COUNT(*) as total FROM imigrantes WHERE naturalidade IS NOT NULL AND naturalidade != 'nan' GROUP BY naturalidade ORDER BY total DESC LIMIT 10"
        df_nat = pd.read_sql(query_nat, cnx)
        
        if not df_nat.empty:
            plt.figure(figsize=(12, 7))
            plt.bar(df_nat['naturalidade'], df_nat['total'], color='teal')
            plt.title('Naturalidades dos Imigrantes (Consulta SQL)')
            plt.xlabel('Naturalidade')
            plt.ylabel('Total')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig('top_naturalidades_barras.png')
            print("Gráfico 'top_naturalidades_barras.png' salvo.")
            
            print("\nEstatísticas das Naturalidades:")
            print(df_nat.describe())

        # 2. Gráfico de Pizza: Distribuição por Estado Civil
        query_civil = "SELECT estado_civil, COUNT(*) as total FROM imigrantes WHERE estado_civil IS NOT NULL AND estado_civil NOT IN ('', 'nan') GROUP BY estado_civil"
        df_civil = pd.read_sql(query_civil, cnx)
        
        if not df_civil.empty:
            plt.figure(figsize=(8, 8))
            plt.pie(df_civil['total'], labels=df_civil['estado_civil'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
            plt.title('Distribuição por Estado Civil (Consulta SQL)')
            plt.savefig('estado_civil_pizza.png')
            print("Gráfico 'estado_civil_pizza.png' salvo.")

        cnx.close()
    except Exception as e:
        print(f"Erro na análise adicional: {e}")

gerar_graficos(df_filtrado, ano_inicio, ano_fim)

if setup_mysql():
    carga_dados_mysql(df_filtrado)
    analise_adicional_mysql()

print("\nProcesso finalizado com sucesso!")
