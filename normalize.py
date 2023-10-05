# # input เข้าฟังชั่นนี้
# # normalization or standardization

# import os
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# # Load and process the first image
# image_path = 'PDR2.jpg'  # Replace with the correct path to your image file
# image = cv2.imread(image_path)

# if image is not None:
#     # Convert to RGB format
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#     # Resize the image to 640x640
#     image = cv2.resize(image, (640, 640))

#     # Normalize the image
#     image_normalized = image.astype(np.float32) / 255.0

#     # Convert to HSV color space
#     image_hsv = cv2.cvtColor(image_normalized, cv2.COLOR_RGB2HSV)

#     # Define HSV crop boundaries (adjust as needed)
#     lower_hsv = np.array([0, 0, 0], dtype=np.uint8)  # Lower bound for HSV
#     upper_hsv = np.array([180, 255, 255], dtype=np.uint8)  # Upper bound for HSV

#     # Create a mask for cropping based on HSV boundaries
#     mask_hsv = cv2.inRange(image_hsv, lower_hsv, upper_hsv)

#     # Apply the mask to the image
#     cropped_image = cv2.bitwise_and(image, image, mask=mask_hsv)

#     # Display the processed images
#     plt.figure(figsize=(20, 4))
#     plt.subplot(1, 3, 1), plt.imshow(image), plt.title("Resized Input")
#     plt.subplot(1, 3, 2), plt.imshow(image_hsv), plt.title("HSV Image")
#     plt.subplot(1, 3, 3), plt.imshow(cropped_image), plt.title("Cropped Image")
#     plt.show()

import os
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

img = cv2.impread('/Users/payuphatboontaokaew/Documents/GitHub/KidneyLifePlus/PDR2.jpg')
plt.imshow(img)


