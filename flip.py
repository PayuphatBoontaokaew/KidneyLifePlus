import cv2
import os
import imgaug as ia
from imgaug import augmenters as iaa

input_folder = "/Users/payuphatboontaokaew/Documents/GitHub/KidneyLifePlus/Cataract"  # Change this to the folder containing your input images
output_folder = "/Users/payuphatboontaokaew/Documents/GitHub/KidneyLifePlus/Cataract-Aug"  # Change this to the folder where you want to save the augmented images
augmented_images_per_input = 4  # Set the number of augmented images per input image

# Define data augmentation parameters
augmentation = iaa.Sequential([
    iaa.Fliplr(0.5),          # Horizontal flip with a 50% chance
    iaa.Flipud(0.5),          # Vertical flip with a 50% chance
    iaa.Rotate((-45, 45)),   # Rotate images by -45 to 45 degrees
    iaa.GaussianBlur(sigma=(0, 1.0)),  # Apply Gaussian blur with a random sigma
    iaa.Add((-10, 10), per_channel=0.5),  # Add random brightness (-10 to 10) to 50% of the images
])

def augment_and_save_images(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    for image_file in image_files:
        # Read the image
        image_path = os.path.join(input_folder, image_file)
        original_image = cv2.imread(image_path)

        # Check if the image was read successfully
        if original_image is None:
            print(f"Unable to read {image_file}. Skipping.")
            continue

        # Generate the specified number of augmented images per input image
        for i in range(augmented_images_per_input):
            # Apply data augmentation to the original image
            augmented_images = augmentation(images=[original_image])

            # Save the augmented images with unique filenames
            for j, augmented_image in enumerate(augmented_images):
                output_path = os.path.join(output_folder, f"aug_{i}_{j}_{image_file}")
                cv2.imwrite(output_path, augmented_image)

                print(f"Augmented {image_file} and saved as {output_path}")

if __name__ == "__main__":
    augment_and_save_images(input_folder, output_folder)
