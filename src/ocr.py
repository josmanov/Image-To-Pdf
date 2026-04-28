from PIL import Image
import pytesseract
import sys
import os


if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

pytesseract.pytesseract.tesseract_cmd = os.path.join(base_path, "tesseract", "tesseract.exe")

def extract_text_data(image_path: str) -> str:
    image = Image.open(image_path)
    data = pytesseract.image_to_data(image)
    
    words = []
    for line in data.strip().split('\n')[1:]:
        parts = line.split('\t')
        if len(parts) == 12:
            level = int(parts[0])
            x, y, width, height,= map(int, parts[6:10])
            conf = int(float(parts[10]))
            text = parts[11]

            if level == 5 and text.strip():
                words.append({
                    'text': text,
                    'x': x,
                    'y': y,
                    'width': width,
                    'height': height,
                    'confidence': conf
                })
    return words
