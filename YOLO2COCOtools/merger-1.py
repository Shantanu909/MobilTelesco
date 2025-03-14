import os
import shutil

# Ask user for source and destination folders
source_folder = input("Enter the source folder path (containing subfolders): ").strip()
destination_folder = input("Enter the destination folder path: ").strip()

# Check if the provided paths exist
if not os.path.exists(source_folder):
    print("❌ Source folder does not exist. Exiting...")
    exit()

os.makedirs(destination_folder, exist_ok=True)  # Create destination folder if it doesn't exist

# Walk through all subfolders and move files
for root, _, files in os.walk(source_folder):
    for file in files:
        file_path = os.path.join(root, file)
        shutil.move(file_path, os.path.join(destination_folder, file))

print(f"✅ All files have been moved to: {destination_folder}")
