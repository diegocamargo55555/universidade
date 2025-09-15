import cv2
import numpy as np

img = 'pontos.png'

imagem = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

kernel = np.array([
        [-1, -1, -1],
        [-1,  8, -1],
        [-1, -1, -1]
    ])

imagem_filtrada = cv2.filter2D(imagem, -1, kernel)

limiar = 200
_, imagem_resultante = cv2.threshold(imagem_filtrada, limiar, 255, cv2.THRESH_BINARY)

cv2.imwrite("2.png", imagem_resultante)

