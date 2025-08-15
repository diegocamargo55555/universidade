import cv2
import numpy as np


img= cv2.imread('./Lista1/lena.png')

c = 255 / np.log(1 + np.max(img))
log_img = c * (np.log(img + 1))


c = c.astype('uint8')
cv2.imshow('Soma de Imagens', log_img)
cv2.imwrite('./Lista1/lena_log.jpg', log_img)  
cv2.waitKey(0)
cv2.destroyAllWindows()

