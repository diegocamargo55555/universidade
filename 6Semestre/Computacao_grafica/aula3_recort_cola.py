import cv2

img = cv2.imread('images.jpeg')

recorte = img[25:100, 35:100]
img[20:95, 10:75] = recorte


cv2.imshow('Recorte', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

