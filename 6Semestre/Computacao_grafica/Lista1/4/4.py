import cv2
import numpy as np

# 1. Carregue a imagem
try:
    img= cv2.imread('../img_aluno.png')
    if img is None:
        raise FileNotFoundError("Imagem não encontrada.")
except FileNotFoundError as e:
    print(e)
    exit()

c = 255 / np.log(1 + np.max(img))
log_img = c * np.log(0.99 + img)
log_img = np.array(log_img, dtype=np.uint8)
log_img = cv2.convertScaleAbs(log_img)

cv2.imshow('Imagem Original', img)
cv2.imshow('Imagem Transformada (Log)', log_img)
cv2.imwrite('img_aluno.jpg', log_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
