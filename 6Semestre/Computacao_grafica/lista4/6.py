import cv2
import numpy as np
import matplotlib.pyplot as plt
import os # Importamos o módulo 'os' para manipular nomes de arquivos

def metodo_otsu(img_gray):
    # 1. Calcular o histograma da imagem
    hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])

    # 2. Normalizar o histograma para obter a distribuição de probabilidade
    total_pixels = img_gray.shape[0] * img_gray.shape[1]
    hist_norm = hist.ravel() / total_pixels

    # Vetor para armazenar a variância entre classes para cada limiar
    variancias_entre_classes = np.zeros(256)
    
    # Intensidade média global
    media_global = np.sum([i * hist_norm[i] for i in range(256)])

    # 3. Iterar por todos os possíveis limiares (t) de 0 a 255
    for t in range(256):
        # Calcular peso (w1) e média (mu1) da classe 1 (fundo)
        w1 = np.sum(hist_norm[:t+1])
        mu1 = np.sum([i * hist_norm[i] for i in range(t+1)])
        
        # Evitar divisão por zero
        if w1 > 0:
            mu1 /= w1
        else: # Se w1 é 0, a média também é 0
            mu1 = 0

        # O peso e a média da classe 2 podem ser calculados a partir dos da classe 1
        w2 = 1 - w1
        
        if w2 > 0:
            # A média da classe 2 é calculada a partir da média global
            mu2 = (media_global - w1 * mu1) / w2
            # 5. Calcular a variância entre classes
            variancias_entre_classes[t] = w1 * w2 * ((mu1 - mu2) ** 2)
        else:
            variancias_entre_classes[t] = 0

    # 6. Encontrar o limiar que maximiza a variância entre classes
    limiar_otsu = np.argmax(variancias_entre_classes)

    # 7. Aplicar o limiar para binarizar a imagem
    _, img_binarizada = cv2.threshold(img_gray, limiar_otsu, 255, cv2.THRESH_BINARY)

    return limiar_otsu, img_binarizada

# --- Função para processar, exibir e SALVAR os resultados ---
def processar_e_mostrar(caminho_imagem):
    """
    Carrega uma imagem, aplica o método de Otsu, exibe os resultados e salva a imagem gerada.
    """
    # Carregar a imagem
    img_color = cv2.imread(caminho_imagem)
    if img_color is None:
        print(f"Erro: Não foi possível carregar a imagem em '{caminho_imagem}'")
        return

    # Converter para tons de cinza
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    # Aplicar o método de Otsu
    limiar, img_otsu = metodo_otsu(img_gray)

    print(f"Processando imagem: {caminho_imagem}")
    print(f"Limiar de Otsu calculado: {limiar}")
    
    # --- ALTERAÇÃO AQUI ---
    # Criar o nome do arquivo de saída e salvar a imagem binarizada
    # Ex: 'harewood.jpg' -> 'harewood_otsu.jpg'
    nome_base, extensao = os.path.splitext(caminho_imagem)
    caminho_saida = f"{nome_base}_otsu{extensao}"
    
    # Salva a imagem no disco
    cv2.imwrite(caminho_saida, img_otsu)
    print(f"Imagem binarizada salva em: {caminho_saida}\n")
    # --- FIM DA ALTERAÇÃO ---

    # Exibir os resultados (funcionalidade mantida)
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB))
    plt.title('Imagem Original')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.hist(img_gray.ravel(), 256)
    plt.axvline(x=limiar, color='r', linestyle='dashed', linewidth=2)
    plt.title(f'Histograma e Limiar de Otsu ({limiar})')
    plt.xlabel('Intensidade')
    plt.ylabel('Frequência')

    plt.subplot(1, 3, 3)
    plt.imshow(img_otsu, cmap='gray')
    plt.title(f'Resultado Salvo em:\n{caminho_saida}') # Título atualizado para mostrar onde foi salvo
    plt.axis('off')

    plt.suptitle(f"Análise da Imagem: {os.path.basename(caminho_imagem)}", fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


# --- Aplicação nas suas imagens ---
# Coloque o nome dos seus arquivos na lista abaixo.
# Certifique-se de que as imagens estão na mesma pasta que o script
# ou forneça o caminho completo para elas.
imagens_para_processar = ["harewood.jpg", "nuts.jpg", "snow.jpg", "img_aluno.png"]

for nome_imagem in imagens_para_processar:
    processar_e_mostrar(nome_imagem)
