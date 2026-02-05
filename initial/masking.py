import cv2
import numpy as np

# Load your image
img = cv2.imread(r"C:\Users\shaik\Desktop\initial\book_5.jpeg")

# Bounding box (your values)
x = 1334.5
y = 2027.5
w = 2215
h = 2177
print(img.shape)

# Convert float coords to int
x, y = int(x), int(y)
w, h = int(w), int(h)

# Create empty mask with same HxW as image
mask = np.zeros(img.shape[:2], dtype=np.uint8)

# Draw white rectangle on mask (region of interest)
mask[y:y+h, x:x+w] = 255

# Apply mask
masked_img = cv2.bitwise_and(img, img, mask=mask)

# Save results
cv2.imwrite("mask.png", mask)
cv2.imwrite("masked_output.png", masked_img)

print("Mask and masked image saved!")
