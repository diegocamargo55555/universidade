import cv2
import numpy as np

def processar_imagem_simples():
    """Versão simplificada usando OpenCV"""
    
    # Carregar imagem
    imagem = cv2.imread('ruidos.png', cv2.IMREAD_GRAYSCALE)
    
    # Binarizar
    _, imagem_bin = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)
    
    # Definir kernel
    kernel = np.ones((3, 3), np.uint8)
    
    # i. Abertura - remove ruídos no fundo
    abertura = cv2.morphologyEx(imagem_bin, cv2.MORPH_OPEN, kernel)
    cv2.imwrite('abertura_resultado.png', abertura)
    
    # ii. Fechamento - remove ruídos no objeto
    fechamento = cv2.morphologyEx(imagem_bin, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite('fechamento_resultado.png', fechamento)
    
    print("Operações concluídas!")
    print("Abertura salva como 'abertura_resultado.png'")
    print("Fechamento salva como 'fechamento_resultado.png'")

# Executar
processar_imagem_simples()