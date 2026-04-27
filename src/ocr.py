from PIL import Image
import pytesseract

def extract_text_data(image_path: str) -> str:
    image = Image.open(image_path)
    data = pytesseract.image_to_data(image)
    
    words = []
    for line in data.strip().split('\n')[1:]:
        parts = line.split('\t')
        if len(parts) == 12:
            level = int(parts[0])
            x, y, width, height, conf = map(int, parts[6:11])
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
