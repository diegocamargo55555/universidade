import cv2
import numpy as np
import matplotlib.pyplot as plt

def calcular_histograma_normalizado(imagem):
    # Garante que a imagem de entrada é válida
    if imagem is None:
        raise ValueError("A imagem de entrada não pode ser nula.")

    # Etapa 1: Calcular o histograma padrão (contagem de pixels)
    # A função do NumPy é uma maneira eficiente de fazer isso.
    hist, _ = np.histogram(imagem.flatten(), bins=256, range=[0, 256])

    # Etapa 2: Obter o número total de pixels na imagem
    total_de_pixels = imagem.size

    # Etapa 3: Normalizar o histograma dividindo cada valor pelo total de pixels
    # Isso converte as contagens em probabilidades
    hist_normalizado = hist / total_de_pixels

    return hist_normalizado

# --- Bloco Principal de Execução ---

# Tenta carregar uma imagem local em escala de cinza.
# Altere 'lena.png' para o nome do seu arquivo de imagem.
nome_do_arquivo = '../lena.png'
try:
    img = cv2.imread(nome_do_arquivo, cv2.IMREAD_GRAYSCALE)
    if img is None:
        # Lança um erro se o arquivo não for encontrado ou não puder ser lido
        raise FileNotFoundError
except FileNotFoundError:
    print(f"Aviso: O arquivo '{nome_do_arquivo}' não foi encontrado.")
    print("Usando uma imagem de gradiente como exemplo.")
    
    # Cria uma imagem de gradiente (preto para branco) para demonstração
    gradiente = np.linspace(0, 255, 256, dtype=np.uint8)
    img = np.tile(gradiente, (256, 1))

# Chama a função para calcular o histograma normalizado
histograma_norm = calcular_histograma_normalizado(img)

# --- Visualização dos Resultados ---
fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# Mostra a imagem de entrada
axes[0].imshow(img, cmap='gray', vmin=0, vmax=255)
axes[0].set_title('Imagem de Entrada')
axes[0].axis('off')

# Mostra o gráfico do histograma normalizado
axes[1].bar(range(256), histograma_norm, color='darkcyan', width=1.0)
axes[1].set_title('Histograma Normalizado')
axes[1].set_xlabel('Nível de Cinza (Intensidade)')
axes[1].set_ylabel('Probabilidade (Frequência Relativa)')
axes[1].set_xlim([0, 255])
axes[1].grid(axis='y', linestyle='--', alpha=0.7)

# Salva a figura em um arquivo e exibe mensagem de sucesso
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('resultado_histograma_normalizado.png')

print("Código executado com sucesso!")
# Verifica se a soma das probabilidades é 1.0
print(f"Soma de verificação do histograma normalizado: {np.sum(histograma_norm):.4f}")
print("O resultado foi salvo como 'resultado_histograma_normalizado.png'.")