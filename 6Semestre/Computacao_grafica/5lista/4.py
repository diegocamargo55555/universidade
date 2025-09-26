import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("cachorro.png", cv2.IMREAD_GRAYSCALE)

_, img_binaria = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((3, 3), np.uint8)

img_erodida = cv2.erode(img_binaria, kernel, iterations=1)
borda_interna = cv2.subtract(img_binaria, img_erodida)
cv2.imwrite('4interna.png', borda_interna)
print("Imagem com borda interna salva como 'cachorro_borda_interna.png'")

img_dilatada = cv2.dilate(img_binaria, kernel, iterations=1)
borda_externa = cv2.subtract(img_dilatada, img_binaria)
cv2.imwrite('4externa.png', borda_externa)
print("Imagem com borda externa salva como 'cachorro_borda_externa.png'")


plt.figure(figsize=(18, 6))
plt.subplot(1, 3, 1)
plt.imshow(img_binaria, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(borda_interna, cmap='gray')
plt.title('Borda Interna')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(borda_externa, cmap='gray')
plt.title('Borda Externa')
plt.axis('off')

plt.show()

