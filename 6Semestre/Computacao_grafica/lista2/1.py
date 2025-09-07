import numpy as np
import cv2
import matplotlib.pyplot as plt

# vamos implementar uma funcao que executa convolucao para todos os pixels (x,y) da imagem
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
    
    
img1 = cv2.imread("img_aluno.png")
img1_pb = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) 

w_med = np.matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])/9.0
print(w_med)

w_rand = w_med
print(w_rand)

img1_wrand = image_convolution(img1_pb, w_rand)

plt.figure(figsize=(12,12)) 
plt.subplot(121)
plt.imshow(img1_pb, cmap="gray", vmin=0, vmax=255)
plt.title("imagem 3")
plt.axis('off')
plt.subplot(122)
plt.imshow(img1_wrand, cmap="gray", vmin=0, vmax=255)
plt.title("imagem 3 convoluída com filtro aleatorio")
plt.axis('off')
plt.savefig("img_aluno1")
