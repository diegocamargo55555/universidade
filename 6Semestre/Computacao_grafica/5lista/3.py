import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("ruidos.png", cv2.IMREAD_GRAYSCALE)

_, img_binaria = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((3, 3), np.uint8)

abertura = cv2.morphologyEx(img_binaria, cv2.MORPH_OPEN, kernel)
cv2.imwrite('3abertura.png', abertura)
print("Imagem com Abertura salva como 'ruidos_resultado_abertura.png'")

fechamento = cv2.morphologyEx(img_binaria, cv2.MORPH_CLOSE, kernel)
cv2.imwrite('3fechamento.png', fechamento)
print("Imagem com Fechamento salva como 'ruidos_resultado_fechamento.png'")


plt.figure(figsize=(18, 6))
plt.subplot(1, 3, 1)
plt.imshow(img_binaria, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(abertura, cmap='gray')
plt.title('Resultado da Abertura')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(fechamento, cmap='gray')
plt.title('Resultado do Fechamento')
plt.axis('off')

plt.show()

