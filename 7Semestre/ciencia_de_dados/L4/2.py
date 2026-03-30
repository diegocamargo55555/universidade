import pandas as pd

def calcular_media_por_categoria(caminho_arquivo, categoria_alvo):
    df = pd.read_csv(caminho_arquivo)
    
    df.columns = df.columns.str.strip().str.lower()
    
    df_filtrado = df[df['categoria'].str.lower() == categoria_alvo.lower()]
    
    if df_filtrado.empty:
        print(f"Aviso: Nenhum produto encontrado na categoria '{categoria_alvo}'.")
        return 0.0
        
    return df_filtrado['preco'].mean()
        

nome_arquivo = "dados_produtos.csv"
categoria_busca = "Eletrônicos"

media_precos = calcular_media_por_categoria(nome_arquivo, categoria_busca)

if media_precos is not None:
    print(f"A média de preço dos produtos da categoria '{categoria_busca}' é: R$ {media_precos:.2f}")