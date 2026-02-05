import torch
import cv2
import numpy as np
from PIL import Image
from transformers import SegformerImageProcessor, SegformerForSemanticSegmentation
from torch import nn

class AIScanner:
    def __init__(self):
        print("Initializing High-Resolution Scanner...")
        self.model_name = "nvidia/segformer-b0-finetuned-ade-512-512"
        self.processor = SegformerImageProcessor.from_pretrained(self.model_name)
        self.model = SegformerForSemanticSegmentation.from_pretrained(self.model_name)
        self.model.eval()

    def find_paper_corners(self, img):
        # 1. Convert to Grayscale and Blur to remove granite noise
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # 2. Thresholding: Paper is white, Granite is dark
        # This creates a solid white mask for the paper
        _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # 3. Use Canny to find the sharp edges of the paper
        edges = cv2.Canny(blur, 50, 150)
        
        # Combine threshold and edges
        combined = cv2.bitwise_and(thresh, thresh, mask=edges)
        combined = cv2.dilate(combined, None, iterations=2)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            return None
        
        # Sort by area and find the largest rectangular-ish contour
        cnts = sorted(contours, key=cv2.contourArea, reverse=True)[:5]
        
        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            
            # If we find 4 points, that's our notebook
            if len(approx) == 4:
                return approx.reshape(4, 2)

        # Fallback: if approx doesn't find 4, get extreme points of the largest area
        c = cnts[0]
        hull = cv2.convexHull(c).reshape(-1, 2)
        rect = np.zeros((4, 2), dtype="float32")
        s = hull.sum(axis=1)
        rect[0] = hull[np.argmin(s)]
        rect[2] = hull[np.argmax(s)]
        diff = np.diff(hull, axis=1)
        rect[1] = hull[np.argmin(diff)]
        rect[3] = hull[np.argmax(diff)]
        return rect

    def process(self, image_path, output_path):
        img_cv = cv2.imread(image_path)
        if img_cv is None:
            print("File not found!")
            return

        print("Stage 1: Neural Segmentation & Edge Snapping...")
        # Get Corners
        corners = self.find_paper_corners(img_cv)
        
        if corners is None:
            print("Failed to find the paper!")
            return

        # Stage 2: Perspective Transform
        print("Stage 2: Rectifying Perspective...")
        
        # Sort corners
        rect = np.zeros((4, 2), dtype="float32")
        s = corners.sum(axis=1)
        rect[0] = corners[np.argmin(s)] # Top Left
        rect[2] = corners[np.argmax(s)] # Bottom Right
        diff = np.diff(corners, axis=1)
        rect[1] = corners[np.argmin(diff)] # Top Right
        rect[3] = corners[np.argmax(diff)] # Bottom Left

        # Calc target dimensions
        (tl, tr, br, bl) = rect
        width_a = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
        width_b = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
        max_w = max(int(width_a), int(width_b))

        height_a = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
        height_b = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
        max_h = max(int(height_a), int(height_b))

        # Destination coordinates for a flat page
        dst = np.array([
            [0, 0],
            [max_w - 1, 0],
            [max_w - 1, max_h - 1],
            [0, max_h - 1]], dtype="float32")

        M = cv2.getPerspectiveTransform(rect, dst)
        warped = cv2.warpPerspective(img_cv, M, (max_w, max_h))

        # Save output
        cv2.imwrite(output_path, warped)
        print(f"Success! Scanned document saved to {output_path}")

if __name__ == "__main__":
    scanner = AIScanner()
    # Correct path for your local Windows machine
    input_path = r"C:\Users\shaik\Desktop\scanner\book_1.jpeg"
    scanner.process(input_path, "scanned_notebook.jpg")