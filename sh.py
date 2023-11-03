import cv2
import numpy as np

# Load an image
image = cv2.imread("/Users/payuphatboontaokaew/Documents/GitHub/KidneyLifePlus/Moderate_Demented/moderate_2.jpg")

# Convert the image to grayscale (optional, depending on your image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Laplacian kernel for sharpening
sharpened_image = cv2.Laplacian(gray, cv2.CV_64F)

# Convert the result back to the original data type
sharpened_image = np.uint8(np.abs(sharpened_image))

# Display the original and sharpened images
cv2.imshow("Original Image", image)
cv2.imshow("Sharpened Image", sharpened_image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
