from pathlib import Path

from PIL import Image
from reportlab.pdfgen import canvas

def prepare_word_boxes(image_path: str, words: list[dict],
                       min_conf: int = 0, font_scale: float = 0.8) -> list[dict]:
    with Image.open(image_path) as img:
        img_w, img_h = img.size

    out = []
    for w in words:
        if w.get("confidence, 0") < min_conf:
            continue
        x, y, width, height = w["x"], w["y"], w["width"], w["height"]
        pdf_x = x
        pdf_y = img_h - (y + height)
        font_size = max(1, int(height * font_scale))
        out.append({
            "text": w["text"],
            "pdf_x": pdf_x,
            "pdf_y": pdf_y,
            "width": width,
            "height": height,
            "font_size": font_size,
            "confidence": w.get("confidence", 0),
        })
    return out
    

def draw_words(pdf: canvas.Canvas, processed_words: list[dict]) -> None:
    pass

def image_to_pdf(image_path: str, words: list[dict] | None = None, output_path: str | None = None) -> str:
    image_file = Path(image_path)

    if not image_file.exists():
        raise FileNotFoundError(f"Image not found: {image_file}")
    
    if output_path is None:
        output_file = image_file.with_suffix(".pdf")
    else:
        output_file = Path(output_path)
    print(output_file)
    with Image.open(image_file) as img:
        width_px, height_px = img.size
    pdf = canvas.Canvas(str(output_file), pagesize=(width_px, height_px))
    pdf.drawImage(
        str(image_file),
        0,
        0,
        width=width_px,
        height=height_px,
        preserveAspectRatio=True,
        mask="auto",
    )
    if words:
        processed = prepare_word_boxes(image_path, words)
        draw_words(pdf, processed)

    pdf.showPage()
    pdf.save()

    return str(output_file)