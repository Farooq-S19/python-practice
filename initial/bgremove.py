import cv2
import numpy as np

# Load original image
image = cv2.imread(r"C:\Users\shaik\Desktop\initial\image.png")

# Load mask (same size as image)
mask = cv2.imread(r"C:\Users\shaik\Desktop\initial\image_mask.png", cv2.IMREAD_GRAYSCALE)

# Ensure mask is 0 or 1 (normalize)
mask = mask / 255.0

# Add extra dimension for broadcasting (H, W, 1)
mask = mask[..., None]

# Apply mask: keep foreground
foreground = image * mask

# Convert to uint8
foreground = foreground.astype(np.uint8)

# Save result
cv2.imwrite("output.png", foreground)

print("Background removed and saved as output.png")
