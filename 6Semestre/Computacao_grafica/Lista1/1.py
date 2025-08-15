import cv2

img= cv2.imread('./Lista1/ihwa.jpeg')

c = img[:,:,0]/3 +img[:,:,1]/3 + img[:,:,2]/3 
c = c.astype('uint8')
cv2.imshow('Soma de Imagens', c)
cv2.imwrite('./Lista1/ihwa_cinza.jpg', c)  # Salva a imagem em escala de cinza
cv2.waitKey(0)
cv2.destroyAllWindows()

