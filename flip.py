import cv2
import os
import imgaug as ia
from imgaug import augmenters as iaa

input_folder = "/Users/payuphatboontaokaew/Documents/GitHub/KidneyLifePlus/Moderate_Demented"
output_folder = "/Users/payuphatboontaokaew/Documents/GitHub/KidneyLifePlus/Moderate-Alz-Aug"
augmented_images_per_input = 20

# Define the desired size
import imgaug.augmenters as iaa

desired_size = (640, 640)

augmentation = iaa.Sequential([
    iaa.Resize({"height": desired_size[0], "width": desired_size[1]}),
    iaa.Fliplr(0.5),
    iaa.Flipud(0.5),
    iaa.Affine(rotate=(-90, 90)),
    iaa.Affine(rotate=180),
    # iaa.Affine(translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)}),
    # iaa.Affine(scale=(0.66, 1.34)),  # Equivalent to 34% maximum zoom
    # iaa.Multiply((0.5, 1.5), per_channel=0.5),
    # iaa.Add((-35, 35)),
    # iaa.GaussianBlur(sigma=(0, 2.0)),
    # iaa.SaltAndPepper(0.02),  # 2% noise
])


def augment_and_save_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        original_image = cv2.imread(image_path)

        if original_image is None:
            print(f"Unable to read {image_file}. Skipping.")
            continue

        for i in range(augmented_images_per_input):
            augmented_images = augmentation(images=[original_image])

            for j, augmented_image in enumerate(augmented_images):
                output_path = os.path.join(output_folder, f"aug_{i}_{j}_{image_file}")
                cv2.imwrite(output_path, augmented_image)

                print(f"Augmented {image_file} and saved as {output_path}")

if __name__ == "__main__":
    augment_and_save_images(input_folder, output_folder)
