import cv2
import numpy as np

img1 = cv2.imread('images.jpeg')
img2 = cv2.imread('imagem_cinza.jpg')

print("image1: {}{}", img1.shape, img1.dtype)
print("image2: {}{}", img2.shape, img2.dtype)


img3 = img1*0.5 + img2*0.5
img3 = img3.astype(np.uint8)

print("image3: {}{}", img3.shape, img3.dtype)

cv2.imshow('Soma de Imagens', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()