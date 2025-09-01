import cv2
import numpy as np


img= cv2.imread('../img_aluno.png', cv2.IMREAD_GRAYSCALE)


cv2.imshow('Imagem Original (lena.png)', img)

planos_de_bits = []

for i in range(8):
    plano = np.bitwise_and(img, 2**i)
    plano_visual = plano * 255
    planos_de_bits.append(plano_visual)
    cv2.imshow(f'Plano de Bit {i}', plano_visual)
    cv2.imwrite(f'img_aluno_plano_de_bit_{i}.png', plano_visual)

cv2.waitKey(0)
cv2.destroyAllWindows()
