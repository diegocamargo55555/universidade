import cv2
import matplotlib
print(matplotlib.__version__)

img= cv2.imread('./Lista1/ihwa.jpeg')

c = 255 - img[:,:,:]

c = c.astype('uint8')
cv2.imshow('Soma de Imagens', c)
cv2.imwrite('./Lista1/ihwa_negativa.jpg', c)  # Salva a imagem em escala de cinza
cv2.waitKey(0)
cv2.destroyAllWindows()

