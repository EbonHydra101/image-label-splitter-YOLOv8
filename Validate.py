import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the directories for train and validation images and labels
train_images_dir = os.path.join(current_dir, "images/train")
train_labels_dir = os.path.join(current_dir, "labels/train")
val_images_dir = os.path.join(current_dir, "images/val")
val_labels_dir = os.path.join(current_dir, "labels/val")

# Function to validate image and label filename matching
def validate_files(image_dir, label_dir):
    image_files = sorted([f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))])
    label_files = sorted([f for f in os.listdir(label_dir) if os.path.isfile(os.path.join(label_dir, f))])

    matched = 0
    mismatched = 0
    mismatched_files = []

    # Check each image file
    for image_file in image_files:
        image_name = os.path.splitext(image_file)[0]  # Remove extension to match base filename
        label_file = image_name + ".txt"  # Assuming label files are .txt

        # Check if label file exists for the image
        if label_file in label_files:
            matched += 1
        else:
            mismatched += 1
            mismatched_files.append(image_file)

    return matched, mismatched, mismatched_files

# Validate both train and validation datasets
train_matched, train_mismatched, train_mismatched_files = validate_files(train_images_dir, train_labels_dir)
val_matched, val_mismatched, val_mismatched_files = validate_files(val_images_dir, val_labels_dir)

# Output the results
print(f"Training set:")
print(f"  Matched: {train_matched}")
print(f"  Mismatched: {train_mismatched}")
print(f"  Mismatched files: {train_mismatched_files}")
print()

print(f"Validation set:")
print(f"  Matched: {val_matched}")
print(f"  Mismatched: {val_mismatched}")
print(f"  Mismatched files: {val_mismatched_files}")
