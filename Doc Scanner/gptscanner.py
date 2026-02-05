import cv2
import numpy as np
from ultralytics import YOLO

class AIScanner:
    def __init__(self):
        print("\nLoading YOLOv8 model (Bose, noob bot ready)...")
        self.model = YOLO("yolov8s.pt")   # detection model

    def process(self, image_path, output_path):
        print("\nReading image...")
        img = cv2.imread(image_path)

        if img is None:
            print("ERROR: Image not found!")
            return

        h, w = img.shape[:2]

        print("Running detection...")
        results = self.model(image_path)[0]

        if len(results.boxes) == 0:
            print("ERROR: No object detected in image.")
            return

        # Get biggest box
        boxes = results.boxes.xyxy.cpu().numpy()
        areas = [(b[2] - b[0]) * (b[3] - b[1]) for b in boxes]
        best = boxes[np.argmax(areas)]
        x1, y1, x2, y2 = map(int, best)

        print("Detected bounding box:", x1, y1, x2, y2)

        # 4 corners
        rect = np.array([
            [x1, y1],  # TL
            [x2, y1],  # TR
            [x2, y2],  # BR
            [x1, y2]   # BL
        ], dtype=np.float32)

        max_w = x2 - x1
        max_h = y2 - y1

        dst = np.array([
            [0, 0],
            [max_w - 1, 0],
            [max_w - 1, max_h - 1],
            [0, max_h - 1]
        ], dtype=np.float32)

        print("Applying perspective transform...")
        M = cv2.getPerspectiveTransform(rect, dst)
        warped = cv2.warpPerspective(img, M, (max_w, max_h))

        cv2.imwrite(output_path, warped)
        print(f"\nDONE! Saved output as {output_path}")
        

# -----------------------------------------
#         THIS IS WHERE YOU RUN IT
# -----------------------------------------
if __name__ == "__main__":
    scanner = AIScanner()  # ← OBJECT CREATED HERE

    # >>> PUT YOUR IMAGE PATH HERE <<<
    input_image = r"C:\Users\shaik\Desktop\scanner\book_1.jpeg"

    # Output image name
    output_image = "flat_result.jpg"

    scanner.process(input_image, output_image)   # ← PROCESS CALLED HERE
