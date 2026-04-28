from pathlib import Path

from src.ocr import extract_text_data
from src.pdf_writer import image_to_pdf

def test_image_to_pdf():
    image_path = "tests/images/variety-fonts.png"
    output_path = "tests/output/variety-fonts.pdf"

    words = extract_text_data(image_path)
    result = image_to_pdf(image_path, words, output_path, False)
    assert Path(result).exists()