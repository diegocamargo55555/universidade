import cv2
import numpy as np

def preencher_regiao(caminho_imagem, seed_point, cor_preenchimento=(0, 255, 0)):
    img = cv2.imread(caminho_imagem)
    if img is None:
        raise FileNotFoundError(f"Erro: O arquivo '{caminho_imagem}' não foi encontrado.")

    img_preenchida = img.copy()

    h, w = img.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)

    cv2.floodFill(img_preenchida, mask, seed_point, cor_preenchimento)

    cv2.imwrite('gato_preenchido.png', img_preenchida)
    print("Imagem com a região preenchida salva como 'gato_preenchido.png'")

    cv2.imshow('Imagem Original', img)
    cv2.imshow('Região Preenchida', img_preenchida)
    cv2.waitKey(0)
    cv2.destroyAllWindows()