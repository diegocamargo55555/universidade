import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- Implementação dos Algoritmos ---

def calcular_histograma_A(imagem):
    """A. Calcula o histograma padrão (contagem de pixels)."""
    # Cria um array de 256 posições para contar cada nível de intensidade.
    hist = np.zeros(256, dtype=int)
    # Itera sobre cada pixel e incrementa a contagem correspondente.
    for linha in imagem:
        for intensidade_pixel in linha:
            hist[intensidade_pixel] += 1
    return hist

def calcular_histograma_B(histograma_A, total_pixels):
    """B. Calcula o histograma normalizado (probabilidades)."""
    # Divide a contagem de cada intensidade pelo número total de pixels.
    return histograma_A / total_pixels

def calcular_histograma_C(histograma_A):
    """C. Calcula o histograma acumulado."""
    # Usa a função cumsum (soma cumulativa) do NumPy.
    return np.cumsum(histograma_A)

def calcular_histograma_D(histograma_C, total_pixels):
    """D. Calcula o histograma acumulado normalizado (CDF)."""
    # Divide o histograma acumulado pelo total de pixels.
    return histograma_C / total_pixels


# --- Bloco Principal de Execução ---

# Tenta carregar a imagem 'img_aluno.jpg'
try:
    img_colorida = cv2.imread('../img_aluno.png', cv2.IMREAD_COLOR)
    if img_colorida is None:
        raise FileNotFoundError
except FileNotFoundError:
    print("Aviso: 'img_aluno.jpg' não encontrada. Gerando uma imagem de exemplo.")
    # Cria uma imagem de exemplo (gradiente escuro para claro)
    img_colorida = np.zeros((300, 400, 3), dtype=np.uint8)
    gradiente = np.linspace(20, 220, 400).astype(np.uint8)
    img_colorida[:, :] = np.tile(gradiente, (300, 1))[:, :, np.newaxis]

# Converte a imagem para níveis de cinza
img_cinza = cv2.cvtColor(img_colorida, cv2.COLOR_BGR2GRAY)

# Calcula o total de pixels para a normalização
total_pixels = img_cinza.size

# Gera os quatro histogramas em sequência
hist_A = calcular_histograma_A(img_cinza)
hist_B = calcular_histograma_B(hist_A, total_pixels)
hist_C = calcular_histograma_C(hist_A)
hist_D = calcular_histograma_D(hist_C, total_pixels)


# --- Visualização dos Resultados ---
fig, axs = plt.subplots(3, 2, figsize=(15, 18))
fig.suptitle('Análise de Histogramas da Imagem', fontsize=20)

# 1. Mostra a Imagem em Níveis de Cinza
axs[0, 0].imshow(img_cinza, cmap='gray', vmin=0, vmax=255)
axs[0, 0].set_title('Imagem em Níveis de Cinza')
axs[0, 0].axis('off')

# Oculta o subplot vazio
axs[0, 1].axis('off')

# 2. Histograma A
axs[1, 0].bar(range(256), hist_A, color='blue', width=1.0)
axs[1, 0].set_title('A. Histograma Padrão')
axs[1, 0].set_xlabel('Nível de Cinza')
axs[1, 0].set_ylabel('Frequência (Nº de Pixels)')
axs[1, 0].set_xlim([0, 255])

# 3. Histograma B
axs[1, 1].bar(range(256), hist_B, color='green', width=1.0)
axs[1, 1].set_title('B. Histograma Normalizado')
axs[1, 1].set_xlabel('Nível de Cinza')
axs[1, 1].set_ylabel('Probabilidade')
axs[1, 1].set_xlim([0, 255])

# 4. Histograma C
axs[2, 0].plot(range(256), hist_C, color='red')
axs[2, 0].set_title('C. Histograma Acumulado')
axs[2, 0].set_xlabel('Nível de Cinza')
axs[2, 0].set_ylabel('Contagem Acumulada de Pixels')
axs[2, 0].set_xlim([0, 255])
axs[2, 0].grid(True, linestyle='--', alpha=0.6)

# 5. Histograma D
axs[2, 1].plot(range(256), hist_D, color='purple')
axs[2, 1].set_title('D. Histograma Acumulado Normalizado (CDF)')
axs[2, 1].set_xlabel('Nível de Cinza')
axs[2, 1].set_ylabel('Probabilidade Acumulada')
axs[2, 1].set_xlim([0, 255])
axs[2, 1].grid(True, linestyle='--', alpha=0.6)


# Ajusta o layout e salva a figura
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('resultados_histogramas.png')

print("Código executado com sucesso.")
print("A imagem com todos os histogramas foi salva como 'resultados_histogramas.png'.")
