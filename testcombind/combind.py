import cv2
import os

# Step 1: Load Images
image_dir = "/Users/payuphatboontaokaew/Documents/GitHub/KidneyLifePlus/capture-img"
image_files = [f for f in os.listdir(image_dir) if f.endswith(".jpg")]

images = []
for image_file in image_files:
    image_path = os.path.join(image_dir, image_file)
    img = cv2.imread(image_path)
    images.append(img)

# Step 2: Image Processing (Gaussian Blur)
processed_images = []
for img in images:
    # Apply Gaussian blur with a 5x5 kernel (you can adjust the kernel size)
    blurred_img = cv2.GaussianBlur(img, (5, 5), 0)
    processed_images.append(blurred_img)

# Step 3: Overlay Images
canvas = processed_images[0].copy()

for img in processed_images[1:]:
    cv2.addWeighted(canvas, 1, img, 1, 0, canvas)

# Step 4: Save the Result
output_path = "overlayed_image.jpg"
cv2.imwrite(output_path, canvas)

# Step 5: Display the Result (optional)
cv2.imshow("Overlayed Image", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Overlayed image saved at:", output_path)
