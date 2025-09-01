import cv2
import matplotlib
print(matplotlib.__version__)

img= cv2.imread('../img_aluno.png')

c = 255 - img[:,:,:]

c = c.astype('uint8')
cv2.imshow('Soma de Imagens', c)
cv2.imwrite('img_aluno_negativa.jpg', c)  
cv2.waitKey(0)
cv2.destroyAllWindows()

