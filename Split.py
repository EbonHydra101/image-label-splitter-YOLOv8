import os
import shutil
from sklearn.model_selection import train_test_split

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Input folders
images_dir = os.path.join(current_dir, "IMG")
labels_dir = os.path.join(current_dir, "LBL")

# Output folders
train_images_dir = os.path.join(current_dir, "images/train")
val_images_dir = os.path.join(current_dir, "images/val")
train_labels_dir = os.path.join(current_dir, "labels/train")
val_labels_dir = os.path.join(current_dir, "labels/val")

# Ensure output directories exist
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

# Collect filenames (assuming images and labels match in name)
image_files = sorted([f for f in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir, f))])
label_files = sorted([f for f in os.listdir(labels_dir) if os.path.isfile(os.path.join(labels_dir, f))])

# Create a dictionary to map image filenames to label filenames (only if label exists)
image_label_map = {}
for image_file in image_files:
    label_file = os.path.splitext(image_file)[0] + ".txt"  # Assuming label files are .txt
    if label_file in label_files:
        image_label_map[image_file] = label_file
    else:
        image_label_map[image_file] = None  # If no label exists, include image with None for label

# Separate images that have corresponding labels for validation
valid_image_label_map = {k: v for k, v in image_label_map.items() if v is not None}

# Split the valid images and labels into 70% training and 30% validation
train_images, val_images = train_test_split(list(valid_image_label_map.keys()), test_size=0.3, random_state=42)

# Function to copy files to their respective folders
def copy_files(file_list, src_dir, dst_dir):
    for file_name in file_list:
        shutil.copy(os.path.join(src_dir, file_name), os.path.join(dst_dir, file_name))

# Copy images and labels to train and val folders
for image_file in train_images:
    copy_files([image_file], images_dir, train_images_dir)
    label_file = image_label_map[image_file]
    if label_file:
        copy_files([label_file], labels_dir, train_labels_dir)

for image_file in val_images:
    copy_files([image_file], images_dir, val_images_dir)
    label_file = image_label_map[image_file]
    if label_file:
        copy_files([label_file], labels_dir, val_labels_dir)

# For images without labels, put them in the train set without labels
for image_file, label_file in image_label_map.items():
    if label_file is None and image_file not in train_images:
        copy_files([image_file], images_dir, train_images_dir)

print("Data successfully split into train and val folders!")
