import cv2

img = cv2.imread('images.jpeg')

print(img.shape)
print(img.size)
print(img.dtype)
print('[B G R]'.format(img[50, 50]) )

img[50:150, 150:250] = [255,33,255]
img[50, 155] = [100, 0, 0]  

cv2.imshow('Pixels', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

