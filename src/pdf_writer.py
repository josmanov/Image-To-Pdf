from pathlib import Path

from PIL import Image
from reportlab.pdfgen import canvas

def image_to_pdf(image_path: str, output_path: str | None = None) -> str:
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
    pdf.showPage()
    pdf.save()

    return str(output_file)