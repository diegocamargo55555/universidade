import numpy as np
import cv2
import matplotlib.pyplot as plt


    
img1 = cv2.imread("img_aluno.png")
img1_pb = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) 

laplacian = cv2.Laplacian(img1_pb,cv2.CV_64F)

plt.figure(figsize=(12,12)) 
plt.subplot(131)
plt.imshow(img1_pb, cmap="gray", vmin=0, vmax=255)
plt.title("Original")
plt.subplot(132)
plt.axis('off')
plt.imshow(laplacian, cmap="gray", vmin=0, vmax=255)
plt.title("Laplace")
plt.axis('off')
plt.savefig("img_aluno4")
