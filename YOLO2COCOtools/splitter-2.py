import os
import shutil
import random

# Get user input for dataset path
dataset_folder = input("Enter the dataset folder path (containing images & labels): ").strip()

# Check if the dataset folder exists
if not os.path.exists(dataset_folder):
    print("❌ Error: The specified folder does not exist. Exiting...")
    exit()

# Get train, val, and test split percentages
train_ratio = float(input("Enter train split percentage (e.g., 0.7 for 70%): ").strip())
val_ratio = float(input("Enter validation split percentage (e.g., 0.15 for 15%): ").strip())
test_ratio = 1 - (train_ratio + val_ratio)  # Ensuring sum = 1

if train_ratio + val_ratio > 1.0:
    print("❌ Error: Split percentages exceed 100%. Exiting...")
    exit()

# Define output directories
train_folder = os.path.join(dataset_folder, "train")
val_folder = os.path.join(dataset_folder, "val")
test_folder = os.path.join(dataset_folder, "test")

# Create subdirectories for images and labels
for split in [train_folder, val_folder, test_folder]:
    os.makedirs(os.path.join(split, "images"), exist_ok=True)
    os.makedirs(os.path.join(split, "labels"), exist_ok=True)

# Get all image files (assuming labels have the same name but with .txt extension)
all_images = [f for f in os.listdir(dataset_folder) if f.endswith(".jpg")]
random.shuffle(all_images)  # Shuffle dataset for randomness

# Compute split sizes
total_images = len(all_images)
train_split = int(train_ratio * total_images)
val_split = int(val_ratio * total_images)

# Assign images to splits
train_files = all_images[:train_split]
val_files = all_images[train_split:train_split + val_split]
test_files = all_images[train_split + val_split:]

# Function to move image and corresponding label
def move_files(file_list, target_folder):
    for img in file_list:
        img_path = os.path.join(dataset_folder, img)
        label_path = os.path.join(dataset_folder, img.replace(".jpg", ".txt"))  # Assuming .txt labels
        
        # Move image
        shutil.move(img_path, os.path.join(target_folder, "images", img))
        
        # Move label (if it exists)
        if os.path.exists(label_path):
            shutil.move(label_path, os.path.join(target_folder, "labels", os.path.basename(label_path)))

# Move files into respective splits
move_files(train_files, train_folder)
move_files(val_files, val_folder)
move_files(test_files, test_folder)

print(f"✅ Dataset split completed!\nTrain: {len(train_files)}\nVal: {len(val_files)}\nTest: {len(test_files)}")
