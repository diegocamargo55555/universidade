import cv2 
from skimage.segmentation import flood, flood_fill

def on_mouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        clicks.append((y,x))
        
roots = cv2.imread('root.jpg', 0)
clicks = []

cv2.namedWindow('Input')
cv2.setMouseCallback('Input', on_mouse, 0, )
cv2.imshow('Input', roots)
cv2.waitKey()
seed = clicks[-1]
crescimento = flood_fill(roots, seed, 0, tolerance=20)
cv2.imshow('Region Growing', crescimento)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('5.png', crescimento)