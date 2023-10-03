# input เข้าฟังชั่นนี้
# import required library
import cv2
import numpy as np
import matplotlib.pyplot as plt
# read the input image in grayscale
img = cv2.imread('/Users/payuphatboontaokaew/Documents/GitHub/KidneyLifePlus/PDR2.jpg',0)
print("Image data before Normalize:\n", img)
normalized = np.zeros((50,50))

# Normalize the image
img_resize = cv2.resize(img,(640,640))
img_normalized = cv2.normalize(img_resize, normalized, 0, 1.0,cv2.NORM_MINMAX, dtype=cv2.CV_32F)

# visualize the normalized image
cv2.imshow('Normalized Image', img_normalized)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Image data after Normalize:\n", img_normalized)

# normalization or standardization


