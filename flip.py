import cv2
import os

input_folder = "/Users/payuphatboontaokaew/Documents/GitHub/KidneyLifePlus/moder"  # Change this to the folder containing your input images
output_folder = "/Users/payuphatboontaokaew/Documents/GitHub/KidneyLifePlus/moder"  # Change this to the folder where you want to save the rewinded images

def rewind_images(input_folder, output_folder):
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

        # Create rewinded versions
        rewinded_left = cv2.flip(original_image, 1)
        rewinded_right = cv2.flip(original_image, 0)
        rewinded_up = cv2.flip(rewinded_left, 0)
        rewinded_down = cv2.flip(rewinded_right, 1)

        # Save the rewinded images
        left_output_path = os.path.join(output_folder, f"left_{image_file}")
        right_output_path = os.path.join(output_folder, f"right_{image_file}")
        up_output_path = os.path.join(output_folder, f"up_{image_file}")
        down_output_path = os.path.join(output_folder, f"down_{image_file}")

        cv2.imwrite(left_output_path, rewinded_left)
        cv2.imwrite(right_output_path, rewinded_right)
        cv2.imwrite(up_output_path, rewinded_up)
        cv2.imwrite(down_output_path, rewinded_down)

        print(f"Rewound {image_file} in all directions.")

if __name__ == "__main__":
    rewind_images(input_folder, output_folder)