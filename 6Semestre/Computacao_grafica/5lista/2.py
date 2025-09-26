import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('quadrados.png', cv2.IMREAD_GRAYSCALE)

kernel_size = 41
kernel = np.ones((kernel_size, kernel_size), np.uint8)
erosao = cv2.erode(img, kernel, iterations=1)
img_final = cv2.dilate(erosao, kernel, iterations=1)


plt.figure(figsize=(18, 6))

plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(erosao, cmap='gray')
plt.title('Após Erosão')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(img_final, cmap='gray')
plt.title('Após Dilatação (Resultado Final)')
plt.axis('off')

plt.show()

# Opcional: Salvar a imagem final
cv2.imwrite('2.png', img_final)
print("Processo concluído. A imagem resultante foi salva como 'quadrados_resultado.png'.")
