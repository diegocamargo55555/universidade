""" 
1Explique a importância da visualização de dados como um primeiro passo em qualquer análise, citando exemplos de insights que podem ser obtidos a partir de histogramas ou matrizes de dispersão.

    R: Ao visualizar os dados é possivel analisar relações entre os dados, graus de relações e 


2Diferencie uma distribuição uniforme de uma distribuição normal. Em qual situação seria mais provável usar um histograma para identificar uma dessas distribuições?

    R: A distribuição uniforme o eixo y fica proximo desde o menor x até o maior, enquanto a normal tem seu pico no centro e vai decaindo quanto mais proximo das extremidades
    
    
3Dado um dataset com valores ausentes em uma coluna numérica, descreva duas estratégias diferentes para tratar esses dados e os prós e contras de cada uma.

    R: é possivel Excluir linhas com valores None ou Voltar ao dado original e tentar reparar o valor ausente ou incorreto
    
    
5Explique por que o redimensionamento (scaling) de dados é crucial em algoritmos de aprendizado de máquina que dependem de cálculo de distâncias, como k-NN ou agrupamento (clustering).

    R: Para que variaveis muto discrepantes que distorcao o resultados, e também para filtrar variaveis que podem ter vindo de falha na notacao ou no sensor
    
    
9Descreva a finalidade do argumento leave=False quando tqdm é utilizado em loops aninhados.
    
    R: o argumento leave=False no tqdm é apagar a barra de progresso da tela assim que o loop é concluído. o tqdm em loops aninhados (um loop executando dentro de outro), esse argumento se torna crucial para manter o terminal limpo e legível


"""
import time
from tqdm import tqdm
import pandas as pd
import numpy as np

#Escreva uma função Python que receba uma lista de strings e, usando o padrão try_or_none, tente converter cada string em um número inteiro, retornando None para strings que não podem ser convertidas.
def ex4(lista_strings):
    def str_para_int(s):
        try:
            return int(s)
        except (ValueError, TypeError):
            return None

    return [str_para_int(item) for item in lista_strings]

#dados = ["10", "abc", "42", "3.14", "100"]
#resultado = ex4(dados)
#print(f"Entrada: {dados}")
#print(f"Saída:   {resultado}")



def ex6():
    from sklearn.preprocessing import StandardScaler

    dados = np.array([
        [180, 75],
        [160, 60],
        [170, 65],
        [190, 90],
        [155, 50]
    ])

    scaler = StandardScaler()

    dados_normalizados = scaler.fit_transform(dados)

    print("Dados Originais (Altura, Peso):")
    print(dados)
    print("\nDados Normalizados (Z-Score):")
    print(dados_normalizados)

    print(f"\nMédia das colunas: {dados_normalizados.mean(axis=0)}")
    print(f"Desvio padrão das colunas: {dados_normalizados.std(axis=0)}")

#ex5()


def ex7():

    total_tarefas = 100

    print("Iniciando processamento pesado...")

    for i in tqdm(range(total_tarefas), desc="Progresso", unit="item"):
        time.sleep(0.05)

    print("\nTarefa concluída com sucesso!")

#ex7()


def ex8():

    frutas = ["Maçã", "Banana", "Laranja", "Uva", "Manga", "Abacaxi"]

    print("Processando lista com índice e barra de progresso...")

    for i, fruta in enumerate(tqdm(frutas, desc="Status")):
        time.sleep(0.5)
        tqdm.write(f"Índice {i}: Processando {fruta}...")

    print("\nConcluído!")


#ex8()

def ex10():

    tqdm.pandas(desc="Processando Linhas")

    df = pd.DataFrame({
        'texto': [f"documento_{i}" for i in range(200)],
        'valores': np.random.randint(1, 100, 200)
    })

    def tarefa_pesada(linha):
        time.sleep(0.02) 
        return linha.upper()

    df['texto_processado'] = df['texto'].progress_apply(tarefa_pesada)

    print("\nProcessamento concluído!")
    print(df.head())

#ex10()

