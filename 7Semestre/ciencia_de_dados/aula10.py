from tqdm.auto import tqdm
from concurrent.futures import ThreadPoolExecutor
import time

def tarefa(x):
    time.sleep(0.05) # Simula uma tarefa demorada
    return x*x

with ThreadPoolExecutor() as executor:
    # Acompanha o progresso da execução de tarefas em paralelo
    results = list(tqdm(executor.map(tarefa, range(50)), total=50, desc="Processando em paralelo"))
