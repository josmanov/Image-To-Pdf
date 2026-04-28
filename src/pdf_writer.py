from pathlib import Path

from PIL import Image
from reportlab.pdfgen import canvas

def prepare_word_boxes(image_path: str, words: list[dict],
                       min_conf: int = 0, font_scale: float = 1.1) -> list[dict]:
    with Image.open(image_path) as img:
        img_h = img.size[1]

    descenders = set("gjpqy,;:")
    avg_height = sum(w["height"] for w in words) / len(words) if words else 1
    font_size = max(1, int(avg_height * font_scale))
    out = []

    for w in words:
        if w.get("confidence", 0) < min_conf:
            continue

        text = w["text"]
        x, y, width, height = w["x"], w["y"], w["width"], w["height"]

        pdf_x = x
        pdf_y = img_h - (y + height)

        chars = [ch for ch in text.lower() if ch.isalpha() or ch in descenders]
        has_descenders = any(ch in descenders for ch in chars)

        if has_descenders:
            box_height = int(height * 0.75)
            box_y = pdf_y + (height - box_height)
        else:
            box_height = height
            box_y = pdf_y

        out.append({
            "text": text,
            "pdf_x": pdf_x,
            "pdf_y": box_y,
            "width": width,
            "height": box_height,
            "font_size": font_size,
            "confidence": w.get("confidence", 0),
        })

    return out
    

def draw_words(pdf: canvas.Canvas, processed_words: list[dict], debug_mode: bool = True) -> None:
    from reportlab.pdfbase.pdfmetrics import getFont

    for p in processed_words:
        font_name = "Helvetica"
        font_size = p["font_size"]
        text = p["text"]

        face = getFont(font_name).face
        ascent = face.ascent / 1000.0
        actual_text_height = font_size * ascent
        if actual_text_height > p["height"]:
            font_size = font_size * (p["height"] / actual_text_height)

        text_width = pdf.stringWidth(text, font_name, font_size)
        if len(text) > 1 and text_width > 0:
            char_space = (p["width"] - text_width) / (len(text) - 1)
        else:
            char_space = 0

        if debug_mode:
            pdf.setStrokeColorRGB(1, 0, 0)
            pdf.rect(p["pdf_x"], p["pdf_y"], p["width"], p["height"], stroke=1, fill=0)

        t = pdf.beginText(p["pdf_x"], p["pdf_y"])
        t.setFont(font_name, font_size)
        t.setCharSpace(char_space)

        if debug_mode:
            t.setTextRenderMode(0)
        else:
            t.setTextRenderMode(3)
            
        t.textOut(text)
        pdf.drawText(t)

        pdf.setFillColorRGB(0, 0, 0)
        pdf.setStrokeColorRGB(0, 0, 0)

def image_to_pdf(image_path: str, words: list[dict] | None = None, output_path: str | None = None, show_boxes: bool = True) -> str:
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
        draw_words(pdf, processed, show_boxes)

    pdf.showPage()
    pdf.save()

    return str(output_file)