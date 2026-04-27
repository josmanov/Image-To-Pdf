from pathlib import Path
from src.ocr import extract_text_data

def test_ocr():
    images_dir = Path("tests/images")

    for image_path in images_dir.iterdir():
        if image_path.is_file():
            print(f"\nTesting: {image_path.name}")
            words = extract_text_data(str(image_path))
            print(words)