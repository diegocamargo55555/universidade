import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

img1 = cv2.imread("img_aluno.png")
img1_pb = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) 

kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
#ao inves de usar a funcao convolucional dos exemplos acima, vc define o valor do filtro e usa no filter2D
img_prewittx = cv2.filter2D(img1_pb, -1, kernelx)
img_prewitty = cv2.filter2D(img1_pb, -1, kernely)
img_prewitt = img_prewittx + img_prewitty

plt.figure(figsize=(12,12)) 
plt.subplot(121)
plt.imshow(img1_pb, cmap="gray", vmin=0, vmax=255)
plt.title("Original")
plt.axis('off')
plt.subplot(122)
plt.imshow(img_prewitt, cmap="gray", vmin=0, vmax=255)
plt.title("Prewitt")
plt.savefig("img_aluno6")
