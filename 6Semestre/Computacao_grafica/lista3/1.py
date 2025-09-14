import numpy as np
import cv2 
from matplotlib import pyplot as plt

img1 = cv2.imread('img_aluno.png', 0)
img2 = cv2.imread('barra4.png', 0)
img3 = cv2.imread('teste.tif', 0)
img4 = cv2.imread('arara.png', 0)

sizes = 64
img1_s = img1
img2_s = img2
img3_s = img3
img4_s = img4




F1s = cv2.dft(np.float32(img1_s),flags = cv2.DFT_COMPLEX_OUTPUT)
F2s = cv2.dft(np.float32(img2_s),flags = cv2.DFT_COMPLEX_OUTPUT)
F3s = cv2.dft(np.float32(img3_s),flags = cv2.DFT_COMPLEX_OUTPUT)
F4s = cv2.dft(np.float32(img4_s),flags = cv2.DFT_COMPLEX_OUTPUT)

n2 = F1s.shape[0]//2
m2 = F1s.shape[1]//2

dft_shift1 = np.fft.fftshift(F1s)
dft_shift2 = np.fft.fftshift(F2s)
dft_shift3 = np.fft.fftshift(F3s)
dft_shift4 = np.fft.fftshift(F4s)

magnitude_spectrum1 = 20*np.log(cv2.magnitude(dft_shift1[:,:,0],dft_shift1[:,:,1]))
magnitude_spectrum2 = 20*np.log(cv2.magnitude(dft_shift2[:,:,0],dft_shift2[:,:,1]))
magnitude_spectrum3 = 20*np.log(cv2.magnitude(dft_shift3[:,:,0],dft_shift3[:,:,1]))
magnitude_spectrum4 = 20*np.log(cv2.magnitude(dft_shift4[:,:,0],dft_shift4[:,:,1]))

plt.figure().set_figheight(16) 
plt.subplot(241)
plt.imshow(img1_s, cmap="gray"); plt.axis('off'); plt.title('Original')
plt.subplot(242)
plt.imshow(img2_s, cmap="gray"); plt.axis('off'); plt.title('Original')
plt.subplot(243)
plt.imshow(img3_s, cmap="gray"); plt.axis('off'); plt.title('Original')
plt.subplot(244)
plt.imshow(img3_s, cmap="gray"); plt.axis('off'); plt.title('Original')

plt.subplot(245)
plt.imshow(magnitude_spectrum1, cmap="gray"); plt.axis('off'); plt.title('filtered')
plt.subplot(246)
plt.imshow(magnitude_spectrum2, cmap="gray"); plt.axis('off'); plt.title('filtered')
plt.subplot(247)
plt.imshow(magnitude_spectrum3, cmap="gray"); plt.axis('off'); plt.title('filtered')
plt.subplot(248)
plt.imshow(magnitude_spectrum4, cmap="gray"); plt.axis('off'); plt.title('filtered')
plt.savefig('1.png') 
