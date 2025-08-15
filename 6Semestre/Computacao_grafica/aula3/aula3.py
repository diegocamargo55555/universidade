



import cv2 
img = cv2.imread('images.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Niveis de Cinza', img)




cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imwrite('imagem_cinza.jpg', img)  # Salva a imagem em escala de cinza
#