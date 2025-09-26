import cv2
import numpy as np

def extrair_componente_conectado(caminho_imagem, seed_point, cor=(0, 255, 255)):
    img = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Erro: O arquivo '{caminho_imagem}' não foi encontrado.")

    h, w = img.shape[:2]
    output_img = np.zeros((h, w, 3), dtype=np.uint8)

    mask = np.zeros((h + 2, w + 2), np.uint8)
    cv2.floodFill(img, mask, seed_point, 255) 

    componente_mask = mask[1:-1, 1:-1]

    output_img[componente_mask == 255] = cor

    cv2.imwrite('quadrado_80px_isolado.png', output_img)
    print("Componente extraído e salvo como 'quadrado_80px_isolado.png'")

    cv2.imshow('Componente Conectado Extraido', output_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

