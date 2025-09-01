import cv2
import numpy as np

try:
    img= cv2.imread('../img_aluno.png')
    if img is None:
        raise FileNotFoundError("Imagem não encontrada.")
except FileNotFoundError as e:
    print(e)
    exit()

img = img.astype('uint8')
img = img.astype(np.float32) / 255.0

imgpotente =  2 * np.power(img, 2) 
imgpotente = np.array(imgpotente * 120, dtype=np.uint8) # sem isso n salva 


cv2.imshow('Imagem Original', img)
cv2.imwrite(f'img_aluno.png', imgpotente)

cv2.imshow('Imagem Transformada (Log)', imgpotente)

cv2.waitKey(0)
cv2.destroyAllWindows()
