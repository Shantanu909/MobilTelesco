import cv2
import numpy as np
from process_raw import DngFile

dng_path = "img.dng"

dng = DngFile.read(dng_path)
print(dng.bit)
rgb1 = dng.postprocess()  # demosaicing by rawpy
cv2.imwrite("rgb1.jpg", rgb1[:, :, ::-1])
rgb2 = dng.demosaicing(poww=1)  # demosaicing with gamma correction 0.3
cv2.imwrite("rgb2.jpg", rgb2[:, :, ::-1])
def exposure(img, stops=0):
    scale = 2.0 ** stops
    img = img.astype(np.float32) * scale
    img = np.clip(img, 0, 255)
    return img.astype(np.uint8)

def contrast(img, contrast_level=0):
    img = img.astype(np.float32) / 255.0      
    midpoint = 0.5 
    strength = contrast_level * 5 
    img = 1 / (1 + np.exp(-strength * (img - midpoint)))
    img = np.clip(img * 255, 0, 255)
    return img.astype(np.uint8)

def filter(img, exposure_stops=0, contrast_level=0):
    # Adjust exposure
    img = exposure(img, exposure_stops)
    # Adjust contrast
    img = contrast(img, contrast_level)
    return img

if __name__ == "__main__":
    original = cv2.imread("rgb2.jpg")
    exposure1 = 0.0 #range -2 to 2
    contrast1 = 0.0 #range -0.4 to 1.4
    exposure1=exposure1+0.25
    contrast1=contrast1+0.95
    adjusted_img = filter(original, exposure_stops=exposure1, contrast_level=contrast1)
    #cv2.imshow("Original", adjusted_img)
    cv2.waitKey(0)
    DngFile.save("C:/Users/HP/Desktop/Mobiltelesco/out.dng", dng.raw, bit=dng.bit, pattern=dng.pattern)
    print(dng.bit)
    print(dng.pattern)
    print(dng.raw)