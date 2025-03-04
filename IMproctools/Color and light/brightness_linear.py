import numpy as np
import cv2
import tifffile as tiff

# Load image
img = cv2.imread('bck.jpg')

# Get min and max values
min_val, max_val = np.min(img), np.max(img)

# Print min and max values
print("Min:", min_val)
print("Max:", max_val)

# Normalize and scale image
scaled_img = (img - min_val) / (max_val - min_val)  # Normalize
scaled_img = np.uint32(scaled_img * 65535)  # Scale to [0, 65535]

# Print scaled image details
print(scaled_img.shape, scaled_img.dtype)
print("Min:", np.min(scaled_img), "Max:", np.max(scaled_img))

# Get user input for transformation
alpha = float(input('* Enter alpha [1/max - 1.0]: '))
beta = float(input('* Enter beta [<1.0]: '))

# Apply linear transformation
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        for c in range(img.shape[2]):
            scaled_img[y, x, c] = np.clip(alpha * img[y, x, c] + beta, min_val, max_val)

# Convert back to original range
scaled_img = np.float32(scaled_img)
scaled_img = (scaled_img / 65535.0) * (max_val - min_val) + min_val

# Display images
cv2.imshow('Original', img)
cv2.imshow('Transformed', scaled_img)
tiff.imwrite('new_light.tif', scaled_img)
cv2.waitKey()
