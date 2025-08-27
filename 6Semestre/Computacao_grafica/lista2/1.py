import cv2
import numpy as np
from matplotlib import pyplot as plt

def image_convolution(f, w, debug=False):
    N,M = f.shape
    n,m = w.shape
    
    a = int((n-1)/2)
    b = int((m-1)/2)

    # obtem filtro invertido
    w_flip = np.flip( np.flip(w, 0) , 1)

    g = np.zeros(f.shape, dtype=np.uint8)

    # para cada pixel:
    for x in range(a,N-a):
        for y in range(b,M-b):
            # obtem submatriz a ser usada na convolucao
            sub_f = f[ x-a : x+a+1 , y-b:y+b+1 ]
            if (debug==True):
                print(str(x)+","+str(y)+" - subimage:\n"+str(sub_f))
            # calcula g em x,y
            g[x,y] = np.sum( np.multiply(sub_f, w_flip)).astype(np.uint8)

    return g

img1 = cv2.imread("lena.png")
#Convertendo BGR para RGB
img1_pb = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) 


w_med = np.matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])/9.0
print(w_med)

img2_media = image_convolution(img1_pb, w_med)

# exibindo imagem original e filtrada por w_med
plt.figure(figsize=(12,12)) 
plt.subplot(121)
plt.imshow(cv2.cvtColor(img1_pb, cv2.COLOR_BGR2RGB), cmap="gray", vmin=0, vmax=255)
plt.title("imagem original, ruidosa")
plt.axis('off')
plt.subplot(122)
plt.imshow(cv2.cvtColor(img2_media, cv2.COLOR_BGR2RGB), cmap="gray", vmin=0, vmax=255)
plt.title("imagem convoluída com filtro de media")
plt.axis('off')
plt.show()