import cv2
import numpy as np

img = 'linhas.png'

imagem_cinza = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

# --- 2. Implementar os 4 Filtros (Kernels) ---
kernel_horizontal = np.array([[-1, -1, -1],
                            [ 2,  2,  2],
                            [-1, -1, -1]])

kernel_p45 = np.array([[-1, -1, 2],
                        [-1,  2,-1],
                        [ 2, -1,-1]])

kernel_vertical = np.array([[-1, 2, -1],
                                [-1, 2, -1],
                                [-1, 2, -1]])

kernel_n45 = np.array([[ 2, -1, -1],
                           [-1,  2, -1],
                           [-1, -1,  2]])

img_horizontal = cv2.filter2D(imagem_cinza, -1, kernel_horizontal)
img_p45 = cv2.filter2D(imagem_cinza, -1, kernel_p45)
img_vertical = cv2.filter2D(imagem_cinza, -1, kernel_vertical)
img_n45 = cv2.filter2D(imagem_cinza, -1, kernel_n45)
limiar = 200
_, img_th_horizontal = cv2.threshold(img_horizontal, limiar, 255, cv2.THRESH_BINARY)
_, img_th_p45 = cv2.threshold(img_p45, limiar, 255, cv2.THRESH_BINARY)
_, img_th_vertical = cv2.threshold(img_vertical, limiar, 255, cv2.THRESH_BINARY)
_, img_th_n45 = cv2.threshold(img_n45, limiar, 255, cv2.THRESH_BINARY)

combinada_1 = cv2.bitwise_or(img_th_horizontal, img_th_p45)
combinada_2 = cv2.bitwise_or(img_th_vertical, img_th_n45)
imagem_final = cv2.bitwise_or(combinada_1, combinada_2)

cv2.imwrite("3.png", imagem_final)

