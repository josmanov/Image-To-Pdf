from pathlib import Path
from src.ocr import extract_text

def test_ocr():
    images_dir = Path("tests/images")

    for image_path in images_dir.iterdir():
        if image_path.is_file():
            print(f"\nTesting: {image_path.name}")
            text = extract_text(str(image_path))
            print(text)