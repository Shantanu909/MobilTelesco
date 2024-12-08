import imageio.v3 as iio
import numpy as np
import cv2

def exposure(img, stops=0):
    scale = 2.0 ** stops
    img = img * scale
    
    return img

def contrast(img, contrast_level=0):
    midpoint = 0.5
    strength = contrast_level * 5
    img = 1 / (1 + np.exp(-strength * (img - midpoint)))  # Sigmoid function
    return img

def filter(img, exposure_stops=0, contrast_level=0):
    img = exposure(img, exposure_stops)
    img = contrast(img, contrast_level)
    return img

if __name__ == "__main__":
    # Load 96-bit TIFF file
    original = iio.imread("test.tif")#.astype(np.float32) / 255.0  # Normalize to [0, 1]
    exposure1 = 1.0  # Range -2 to 2
    contrast1 = 0.0  # Range -0.4 to 1.4

    # Process the image
    adjusted_img = filter(original, exposure_stops=exposure1, contrast_level=contrast1)
    # Convert back to 96-bit range (32-bit per channel) and save as TIFF
    adjusted_img = (adjusted_img * 526.0).astype(np.float32)
    iio.imwrite("br_ct.tiff", adjusted_img)
    # Displaying (convert to 8-bit for visualization)
    # display_img = (adjusted_img * 255).astype(np.float16)
    # cv2.imshow("Adjusted Image", display_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
