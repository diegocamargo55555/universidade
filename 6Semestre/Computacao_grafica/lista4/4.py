import cv2

img = 'igreja.png'

imagem = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

imagem_suavizada = cv2.GaussianBlur(imagem, (5, 5), 0)
limiar1 = 100
limiar2 = 200
    
bordas = cv2.Canny(imagem_suavizada, limiar1, limiar2)

cv2.imwrite('4.png', bordas)