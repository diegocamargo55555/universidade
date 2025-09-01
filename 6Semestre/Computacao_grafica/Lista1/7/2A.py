import numpy as np
import cv2
import matplotlib.pyplot as plt

def calcular_histograma(canal_da_imagem):
    histograma = np.zeros(256, dtype=int)
    for linha in canal_da_imagem:
        for pixel_intensidade in linha:
            histograma[pixel_intensidade] += 1

    return histograma

try:
    img_bgr = cv2.imread('../img_aluno.png', cv2.IMREAD_COLOR)
    if img_bgr is None:
        raise FileNotFoundError
except FileNotFoundError:
    print("Aviso: 'unequalized.jpg' não encontrado. Gerando uma imagem de exemplo.")
    img_bgr = np.zeros((256, 256, 3), dtype=np.uint8)
    gradiente = np.linspace(0, 255, 256).astype(np.uint8)
    img_bgr[:, :, 2] = np.tile(gradiente, (256, 1)) # Gradiente Vermelho
    img_bgr[:, :, 1] = np.tile(gradiente[::-1], (256, 1)) # Gradiente Verde (invertido)
    img_bgr[0:128, :, 0] = 200 # Metade superior Azul forte


b, g, r = cv2.split(img_bgr)

hist_canal_vermelho = calcular_histograma(r)
#hist_canal_vermelho = calcular_histograma(g)
#hist_canal_vermelho = calcular_histograma(b)


fig, axes = plt.subplots(1, 2, figsize=(15, 6))

img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

axes[0].imshow(img_rgb)
axes[0].set_title('Imagem de Entrada (Colorida)')
axes[0].axis('off')

axes[1].plot(hist_canal_vermelho, color='red', label='Canal R')
axes[1].set_title('Histogramas dos Canal R')
axes[1].set_xlabel('Intensidade (0-255)')
axes[1].set_ylabel('Frequência (Nº de Pixels)')
axes[1].set_xlim([0, 255])
axes[1].grid(axis='y', linestyle='--', alpha=0.7)
axes[1].legend() 

plt.tight_layout()
plt.savefig('histograma_R.png')

print("Código executado com sucesso.")
print("A imagem com os histogramas dos canais R, G e B foi salva como 'histograma_RGB.png'.")
