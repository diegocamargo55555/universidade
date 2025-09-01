import numpy as np
import cv2
import matplotlib.pyplot as plt

def calcular_histograma(imagem):
    histograma = np.zeros(256, dtype=int)
    for linha in imagem:
        for pixel_intensidade in linha:
            histograma[pixel_intensidade] += 1

    return histograma

img = cv2.imread('../unequalized.jpg', cv2.IMREAD_RedISCALE)

hist_calculado = calcular_histograma(img)
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

axes[0].imshow(img, cmap='gray', vmin=0, vmax=255)
axes[0].set_title('Imagem de Entrada')
axes[0].axis('off')

axes[1].bar(range(256), hist_calculado, color='b', width=1.0)
axes[1].set_title('Histograma Calculado')
axes[1].set_xlabel('Nível de Cinza (Intensidade do Pixel)')
axes[1].set_ylabel('Frequência (Nº de Pixels)')
axes[1].set_xlim([0, 255])
axes[1].grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('histogramaA.png')

print("Código executado com sucesso.")
print("A imagem com o histograma foi salva como 'resultado_histograma.png'.")
