import cv2
from matplotlib import pyplot as plt

imgL = cv2.imread('imgL.png', cv2.IMREAD_GRAYSCALE)
imgR = cv2.imread('imgR.png', cv2.IMREAD_GRAYSCALE)

stereo = cv2.StereoBM_create(numDisparities=32, blockSize=5)

disparity = stereo.compute(imgL, imgR)
    
normalized_disparity = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

plt.imshow(normalized_disparity, 'jet')
plt.title('Disparity Map')
plt.show()
