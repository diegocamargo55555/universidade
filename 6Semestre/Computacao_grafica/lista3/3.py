import numpy as np
import cv2 
from matplotlib import pyplot as plt



img1 = cv2.imread('img_aluno.png', 0)


sizes = 64
img1_s = img1


F1s = cv2.dft(np.float32(img1_s),flags = cv2.DFT_COMPLEX_OUTPUT)
n2 = F1s.shape[0]//2
m2 = F1s.shape[1]//2


rows1 = F1s.shape[0]//2
cols1 = F1s.shape[1]//2


F1p = np.fft.fftshift(F1s).copy()


F1p = np.fft.ifftshift(F1p)

F1p = F1s.copy()
F1p[5:-5,5:-5] = 0 # band stop filter
F1p = np.fft.ifftshift(F1p)

img_back = cv2.idft(F1p)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(121),plt.imshow(img1_s, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('band stop filter'), plt.xticks([]), plt.yticks([])
plt.savefig('3.png') 

plt.show()
