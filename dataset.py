import cv2
import numpy as np

# Load an example image
image = cv2.imread('/Users/payuphatboontaokaew/Documents/GitHub/KidneyLifePlus/cataract_001_png.rf.09cac0afd6943046d4eecfac0677b015 copy.jpg')  # Replace with the path to your image

# Define a function for random rotation
def random_rotation(image, angle_range=(-10, 10)):
    angle = np.random.uniform(angle_range[0], angle_range[1])
    h, w = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))
    return rotated_image

# Define a function for horizontal flip
def horizontal_flip(image, probability=0.5):
    if np.random.rand() < probability:
        return cv2.flip(image, 1)
    else:
        return image

# Define a function for brightness adjustment
def adjust_brightness(image, brightness_factor_range=(0.7, 1.3)):
    brightness_factor = np.random.uniform(brightness_factor_range[0], brightness_factor_range[1])
    return cv2.convertScaleAbs(image, alpha=brightness_factor, beta=0)

# Perform data augmentation
augmented_images = []
for _ in range(10):  # Perform augmentation 10 times
    augmented_image = random_rotation(image)
    augmented_image = horizontal_flip(augmented_image)
    augmented_image = adjust_brightness(augmented_image)
    augmented_images.append(augmented_image)

# Save or use the augmented images as needed
for i, augmented_image in enumerate(augmented_images):
    cv2.imwrite(f'augmented_image_{i}.jpg', augmented_image)
