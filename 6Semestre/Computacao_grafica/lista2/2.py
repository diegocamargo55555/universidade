import numpy as np
import cv2
import matplotlib.pyplot as plt

# vamos implementar uma funcao que executa convolucao para todos os pixels (x,y) da imagem
def image_convolution(f, tamanho_janela, k, debug=False):
    N, M = f.shape
    a = int((tamanho_janela - 1) / 2)
    
    g = np.zeros(f.shape, dtype=np.uint8)

    for x in range(a, N - a):
        for y in range(a, M - a):
            janela = f[x-a : x+a+1, y-a:y+a+1]
            
            valor_central = f[x, y]
            
            vizinhos = janela.flatten()
            
            diferencas = np.abs(vizinhos.astype(np.int16) - int(valor_central))
            
            indices_ordenados = np.argsort(diferencas)
            
            vizinhos_ordenados = vizinhos[indices_ordenados]
            
            k_vizinhos_proximos = vizinhos_ordenados[:k]
            
            media_k = np.mean(k_vizinhos_proximos)
            g[x, y] = np.round(media_k).astype(np.uint8)
    return g
    
    
img1 = cv2.imread("img_aluno.png")
img1_pb = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) 

img1_wrand = image_convolution(img1_pb, 5, 12)

plt.figure(figsize=(12,12)) 
plt.subplot(121)
plt.imshow(img1_pb, cmap="gray", vmin=0, vmax=255)
plt.title("imagem 3")
plt.axis('off')
plt.subplot(122)
plt.imshow(img1_wrand, cmap="gray", vmin=0, vmax=255)
plt.title("imagem 3 convoluída com filtro aleatorio")
plt.axis('off')
plt.savefig("img_aluno2")
