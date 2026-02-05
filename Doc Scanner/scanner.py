from doctr.io import DocumentFile
from doctr.models import ocr_predictor

# Load the OCR model with pretrained parameters
# This will download pre-trained models hosted by Mindee
model = ocr_predictor(pretrained=True)

# Load your document (image or PDF)
# Example for an image file:
doc = DocumentFile.from_images(r"C:\Users\shaik\Desktop\Doc Scanner\IMG_20260204_105313.jpg.jpeg") 

# Example for a PDF file:
# doc = DocumentFile.from_pdf("/path/to/your/document.pdf")

# Analyze the document
result = model(doc)

# Print the extracted text and related info
print(result) 
result.export()
# You can also use result.export() to get a JSON output
