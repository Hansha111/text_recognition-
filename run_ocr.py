import os
from paddleocr import PaddleOCR

# Initialize OCR
ocr = PaddleOCR(use_angle_cls=True, lang="en")

# Define the image path
image_path = r"C:\Users\mayar\OneDrive\Desktop\OCR_2\venv\image.png"

# Check if the file exists
if not os.path.exists(image_path):
    print(f"Error: File '{image_path}' not found! Check the path.")
else:
    # Run OCR if the file exists
    result = ocr.ocr(image_path, cls=True)
    
    extracted_text = [word[1][0] for line in result for word in line]
    print("\nExtracted Text:\n", "\n".join(extracted_text))
    
    
    