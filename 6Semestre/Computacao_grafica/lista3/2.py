import numpy as np
import cv2 
from matplotlib import pyplot as plt



img1 = cv2.imread('teste.tif', 0)


sizes = 64
img1_s = img1


F1s = cv2.dft(np.float32(img1_s),flags = cv2.DFT_COMPLEX_OUTPUT)
n2 = F1s.shape[0]//2
m2 = F1s.shape[1]//2


rows1 = F1s.shape[0]//2
cols1 = F1s.shape[1]//2


F1p = np.fft.fftshift(F1s).copy()
F1p[:n2-9, :] = 0 # square low pass filter, removes higher frequencies
F1p[:, :m2-9] = 0 # square low pass filter, removes higher frequencies
F1p[n2+9:, :] = 0 # square low pass filter, removes higher frequencies
F1p[:, m2+9:] = 0 # square low pass filter, removes higher frequencies
F1p = np.fft.ifftshift(F1p)

F2p = np.fft.fftshift(F1s).copy()
F2p[n2-9:n2+9, m2-9:m2+9] = 0 # square high pass filter, removes first frequencies
F2p = np.fft.ifftshift(F2p)


img_back = cv2.idft(F1p)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

img_back2 = cv2.idft(F2p)
img_back2 = cv2.magnitude(img_back2[:,:,0], img_back2[:,:,1])

plt.subplot(131),plt.imshow(img1_s, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('passa baixa'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back2, cmap = 'gray')
plt.title('passa alta'), plt.xticks([]), plt.yticks([])

plt.savefig('2.png') 

plt.show()
