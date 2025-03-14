import os
import json
import random
import cv2
import matplotlib.pyplot as plt

# Select dataset split
dataset_folder = input("Enter the dataset folder path (containing train, val, test folders): ").strip()
split = random.choice(["train","test","val"])  # Randomly pick a split

# Load COCO annotations
json_path = os.path.join(dataset_folder, split, "annotations.json")
if not os.path.exists(json_path):
    print(f"❌ Error: {json_path} not found. Exiting...")
    exit()

with open(json_path, "r") as f:
    coco_data = json.load(f)

# Pick a random image
image_info = random.choice(coco_data["images"])
image_id = image_info["id"]
image_name = image_info["file_name"]
image_path = os.path.join(dataset_folder, split, "images", image_name)

if not os.path.exists(image_path):
    print(f"❌ Error: Image {image_name} not found at {image_path}. Exiting...")
    exit()

# Find annotations for the selected image
annotations = [ann for ann in coco_data["annotations"] if ann["image_id"] == image_id]

# Load the image
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for plotting

# Draw bounding boxes
for ann in annotations:
    x, y, w, h = map(int, ann["bbox"])
    class_id = ann["category_id"]

    class_name = next((cat["name"] for cat in coco_data["categories"] if cat["id"] == class_id), "Unknown")


    # Draw rectangle
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(image, class_name, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

# Show the image with annotations
plt.figure(figsize=(8, 6))
plt.imshow(image)
plt.axis("off")
plt.title(f"Image: {image_name} (Dataset: {split})")
plt.show()
