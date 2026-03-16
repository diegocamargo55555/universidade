import numpy as np


def estatisticas(x):
    media = x.sum() / len(x)
    min = x.min()
    max = x.max()
    dicionario = {
        "media": media,
        "minimo": min,
        "maximo": max
    }
    return dicionario
    
    
numeros = np.array([12, 32, 54, 23, 634,-99])
print(estatisticas(numeros))
