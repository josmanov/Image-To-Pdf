from pathlib import Path

from src.pdf_writer import image_to_pdf

def test_iamge_to_pdf():
    image_path = "tests/images/letter.webp"
    output_path = "tests/output/letter_out.pdf"

    result = image_to_pdf(image_path, output_path)
    assert Path(result).exists()