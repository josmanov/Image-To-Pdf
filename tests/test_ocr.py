from src.ocr import extract_text

def test_ocr():
    image_path = "tests/images/hello_world.png"
    text = extract_text(image_path)
    print(text)
    image_path = "tests/images/python_function.png"
    text = extract_text(image_path)
    print(text)