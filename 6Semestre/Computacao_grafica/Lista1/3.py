import cv2

img= cv2.imread('./Lista1/lena.png')

# (r-a) (d-c)/(b-a) + c
c = cv2.normalize(img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

cv2.imshow('Soma de Imagens', c)
cv2.imwrite('./Lista1/Lena_cinza.jpg', c)  # Salva a imagem em escala de cinza
cv2.waitKey(0)
cv2.destroyAllWindows()




