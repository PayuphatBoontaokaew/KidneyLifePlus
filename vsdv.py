import shutil

# Source path (the file you want to copy)
source_path = "/Users/payuphatboontaokaew/Documents/GitHub/KidneyLifePlus/img/source_file.jpg"

# Destination path (where you want to save the file on your Mac)
destination_path = "/Users/payuphatboontaokaew/Documents/GitHub/KidneyLifePlus/img/destination_file.jpg"

# Copy the file to the destination
shutil.copy(source_path, destination_path)

print(f"File copied from {source_path} to {destination_path}")
