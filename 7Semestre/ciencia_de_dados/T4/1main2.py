import pandas as pd
import os
from regressao_linear_simples import executar_regressao_simples
from regressao_linear_multipla import executar_regressao_multipla
from regressao_logistica import executar_regressao_logistica
from knn import executar_knn

def carregar_dados():
    caminho_dados = 'Luso_filtrado.json'

    df = pd.read_json(caminho_dados)
    # Pré-processamento
    df = df.dropna(subset=['IDADE', 'ANO_CHEGADA', 'ANO_REGISTRO', 'ESTADO_CIVIL']).copy()
    df = df[(df['IDADE'] >= 0) & (df['IDADE'] <= 100)]
    #df = df['IDADE'] <= 100
    df['IS_SOLTEIRO'] = df['ESTADO_CIVIL'].apply(lambda x: 1 if str(x).strip().lower() == 'solteiro' else 0)
    
    print(f"Dados carregados e pré-processados: {len(df)} registros.")
    return df

def main():
    print("a")
    df = carregar_dados()

    executar_regressao_simples(df)
    executar_regressao_multipla(df)
    executar_regressao_logistica(df)
    executar_knn(df)
    
    print("\nTodos os modelos foram executados com sucesso")

if __name__ == "__main__":
    main()
