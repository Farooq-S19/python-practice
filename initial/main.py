import cv2
import numpy as np

# ---------- STEP 1: Load Images ----------
original = cv2.imread(r"C:\Users\shaik\Desktop\initial\image.png")
mask = cv2.imread(r"C:\Users\shaik\Desktop\initial\image_mask.png", 0)
print(original.shape)
print(mask.shape)

# ---------- STEP 2: Threshold Mask ----------
_, thresh = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)

# ---------- STEP 3: Get Largest Contour ----------
cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnt = max(cnts, key=cv2.contourArea)

# ---------- STEP 4: Approx as Quadrilateral ----------
epsilon = 0.02 * cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)

if len(approx) != 4:
    print("Mask does NOT contain a 4-sided shape ❌")
    exit()

corners = approx.reshape(4, 2).astype(np.float32)

# ---------- STEP 5: Order the corners ----------
# Helper function
def order_points(pts):
    ordered = np.zeros((4, 2), dtype="float32")
    
    s = pts.sum(axis=1)
    ordered[0] = pts[np.argmin(s)]   # top-left
    ordered[2] = pts[np.argmax(s)]   # bottom-right
    
    diff = np.diff(pts, axis=1)
    ordered[1] = pts[np.argmin(diff)]  # top-right
    ordered[3] = pts[np.argmax(diff)]  # bottom-left
    
    return ordered

src = order_points(corners)

# ---------- STEP 6: Compute Width & Height ----------
(w, h) = (original.shape[1], original.shape[0])

dst = np.float32([
    [0, 0],
    [w-1, 0],
    [w-1, h-1],
    [0, h-1]
])

# ---------- STEP 7: Apply Perspective Transform ----------
M = cv2.getPerspectiveTransform(src, dst)
warped = cv2.warpPerspective(original, M, (w, h))

# ---------- STEP 8: Save Output ----------
cv2.imwrite("corrected_output.jpg", warped)

print("Saved corrected_output.jpg")

