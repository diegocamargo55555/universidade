import numpy as np

#1
semana = np.random.randint(-25, 45, size=(25))
#print(semana)
#print("temp media",semana.mean())
#print("temp max", semana.max())


#2 




#3
pontuacoes = np.random.randint(0, 100, size=(10))
#print("pontuacoes media",pontuacoes.mean())
#print("pontuacoes max", pontuacoes.max())


#4
for i in range(20):
    sensor = np.random.rand()
    print(sensor if sensor > 0.7 else "")
    
#5
acoes = np.random.randint (100, 120, size=(5))
