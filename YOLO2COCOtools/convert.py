import os
import json
import cv2

def yolo_to_coco(yolo_annotations, img_width, img_height):
    """ Convert YOLO format to COCO format for a single image """
    coco_annotations = []
    annotation_id = 0  # Unique annotation ID counter

    for line in yolo_annotations:
        parts = line.strip().split()
        class_id = int(parts[0]) + 1  # COCO requires 1-based class indexing
        x_center, y_center, width, height = map(float, parts[1:])

        # Convert YOLO (normalized) bbox to absolute pixel values
        x_min = int((x_center - width / 2) * img_width)
        y_min = int((y_center - height / 2) * img_height)
        bbox_width = int(width * img_width)
        bbox_height = int(height * img_height)

        # Ensure bounding box stays within image bounds
        x_min = max(0, x_min)
        y_min = max(0, y_min)
        bbox_width = min(img_width - x_min, bbox_width)
        bbox_height = min(img_height - y_min, bbox_height)

        # COCO annotation structure
        annotation = {
            "id": annotation_id,
            "category_id": class_id,
            "bbox": [x_min, y_min, bbox_width, bbox_height],
            "area": bbox_width * bbox_height,
            "iscrowd": 0
        }
        coco_annotations.append(annotation)
        annotation_id += 1

    return coco_annotations

def convert_dataset(dataset_path):
    """ Convert a dataset from YOLO format to COCO format while handling different image sizes """
    coco_output = {
        "images": [],
        "annotations": [],
        "categories": []
    }

    # Load class names from classes.txt
    classes_path = os.path.join(dataset_path, "classes.txt")
    if not os.path.exists(classes_path):
        print("❌ Error: classes.txt not found.")
        return

    with open(classes_path, "r") as f:
        class_names = [line.strip() for line in f.readlines()]

    # Add categories to COCO output
    for i, class_name in enumerate(class_names, start=1):
        coco_output["categories"].append({"id": i, "name": class_name})

    # Process each image in the dataset
    img_dir = os.path.join(dataset_path, "images")
    label_dir = os.path.join(dataset_path, "labels")

    annotation_id = 0  # Global annotation ID counter

    for img_file in os.listdir(img_dir):
        if not img_file.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        img_path = os.path.join(img_dir, img_file)
        label_path = os.path.join(label_dir, img_file.replace(".jpg", ".txt").replace(".png", ".txt"))

        # Load image to get its dimensions
        img = cv2.imread(img_path)
        if img is None:
            print(f"❌ Error loading image {img_file}")
            continue

        img_height, img_width, _ = img.shape
        image_id = len(coco_output["images"]) + 1

        # Store image info in COCO format
        coco_output["images"].append({
            "id": image_id,
            "file_name": img_file,
            "width": img_width,
            "height": img_height
        })

        # Process annotations (if the label file exists)
        if os.path.exists(label_path):
            with open(label_path, "r") as f:
                yolo_annotations = f.readlines()

            coco_annotations = yolo_to_coco(yolo_annotations, img_width, img_height)
            for ann in coco_annotations:
                ann["image_id"] = image_id
                ann["id"] = annotation_id  # Assign unique annotation ID
                coco_output["annotations"].append(ann)
                annotation_id += 1  # Increment annotation ID

    # Save COCO dataset to a JSON file
    output_json = os.path.join(dataset_path, "annotations.json")
    with open(output_json, "w") as f:
        json.dump(coco_output, f, indent=4)
    
    print(f"✅ COCO dataset saved at {output_json}")

# Run the conversion
dataset_folder = input("Enter dataset folder path: ")
convert_dataset(dataset_folder)
