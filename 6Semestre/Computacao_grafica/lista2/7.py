import numpy as np
import cv2
import matplotlib.pyplot as plt
import math


    
img1 = cv2.imread("img_aluno.png")
img1_pb = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) 

img_sobelx = cv2.Sobel(img1_pb,cv2.CV_8U,1,0,ksize=5)
img_sobely = cv2.Sobel(img1_pb,cv2.CV_8U,0,1,ksize=5)
sobel = img_sobelx + img_sobely

plt.figure(figsize=(12,12)) 
plt.subplot(122)
plt.imshow(sobel, cmap="gray", vmin=0, vmax=255)
plt.title("Sobel")
plt.axis('off')

plt.subplot(121)
plt.imshow(img1_pb, cmap="gray", vmin=0, vmax=255)
plt.title("Original")
plt.savefig("img_aluno7")




















