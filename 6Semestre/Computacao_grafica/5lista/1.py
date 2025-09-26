import cv2
import numpy as np
import matplotlib.pyplot as plt

imagem = np.array(  [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,255,255,255,255,0,0,0,0,255,255,255,0,0,0],
                    [0,0,0,255,255,255,255,0,255,255,255,255,255,255,0,0,0],
                    [0,0,0,255,255,255,255,255,255,255,255,255,255,255,0,0,0],
                    [0,0,0,0,255,0,0,0,0,255,255,255,255,255,0,0,0],
                    [0,0,0,0,255,0,0,0,0,255,255,0,255,255,0,0,0],
                    [0,0,0,0,0,0,0,0,0,255,255,0,255,255,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],np.uint8
)
arrayA = np.array([[255, 255, 255],
                   [255, 255, 255],
                   [255, 255, 255]], np.uint8)

arrayB = np.array([[255, 0, 255],
                   [0, 0, 0],
                   [255, 0, 255]],np.uint8)

erosaoA = cv2.erode(imagem, arrayA, iterations=1)
erosaoB = cv2.erode(imagem, arrayB, iterations=1)
cv2.imwrite('1A.png', erosaoA)
cv2.imwrite('1B.png', erosaoB)

plt.figure(figsize=(9,9)) 
plt.subplot(311)
plt.imshow(imagem, cmap="gray", vmin=0, vmax=255)
plt.title("imagem original, ruidosa")
plt.axis('off')
plt.subplot(312)
plt.imshow(erosaoA, cmap="gray", vmin=0, vmax=255)
plt.title("imagem convoluída com filtro 1")
plt.axis('off')
plt.subplot(313)
plt.imshow(erosaoB, cmap="gray", vmin=0, vmax=255)
plt.title("imagem convoluída com filtro 2")
plt.axis('off')
plt.show()