import os

# Path to YOLO annotation files
annotations_dir = r"C:\Users\HP\Downloads\windows_v1.8.1\windows_v1.8.1\dataset\labels\val"

# Remap classes
class_mapping = {15: 0, 16: 1}  # Old class indices to new class indices

for filename in os.listdir(annotations_dir):
    if not filename.endswith(".txt"):
        continue

    file_path = os.path.join(annotations_dir, filename)
    updated_lines = []

    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split()
            class_id = int(parts[0])
            if class_id in class_mapping:
                parts[0] = str(class_mapping[class_id])  # Update class ID
                updated_lines.append(" ".join(parts))

    # Save the updated file
    with open(file_path, "w") as file:
        file.write("\n".join(updated_lines))
