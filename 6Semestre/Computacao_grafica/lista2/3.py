import numpy as np
import cv2
import matplotlib.pyplot as plt

def image_convolution(f, tamanho_janela):    
    N, M = f.shape
    a = int((tamanho_janela - 1) / 2)
    
    g = np.zeros(f.shape, dtype=np.uint8)

    for x in range(a, N - a):
        for y in range(a, M - a):
            janela = f[x-a : x+a+1, y-a:y+a+1]
            valor_mediano = np.median(janela)
            
            g[x, y] = np.round(valor_mediano).astype(np.uint8)
        
    return g


img1 = cv2.imread("img_aluno.png")
img1_pb = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) 

tamanho_janela = 5
img_mediana = image_convolution(img1_pb, tamanho_janela)

plt.figure(figsize=(18, 6)) 

plt.subplot(131)
plt.imshow(img1_pb, cmap="gray", vmin=0, vmax=255)
plt.title("Original em Tons de Cinza")
plt.axis('off')

plt.subplot(132)
plt.imshow(img_mediana, cmap="gray", vmin=0, vmax=255)
plt.title(f"Filtro de Mediana (Janela {tamanho_janela}x{tamanho_janela})")
plt.axis('off')
    
plt.tight_layout()
plt.savefig("img_aluno3.png")
print("Figura comparativa guardada como 'img_aluno3.png'")

