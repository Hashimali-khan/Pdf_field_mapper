from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io
import os

def draw_grid_overlay(filename):
    """Create a PDF with a coordinate grid overlay."""
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    for x in range(0, 600, 20):
        can.drawString(x + 2, 5, str(x))
        can.line(x, 0, x, 800)
    for y in range(0, 800, 20):
        can.drawString(2, y + 2, str(y))
        can.line(0, y, 600, y)
    can.save()
    packet.seek(0)
    with open(filename, "wb") as f:
        f.write(packet.read())

def merge_overlay(base_pdf, overlay_pdf, output_pdf):
    """Merge the overlay PDF onto each page of the base PDF."""
    try:
        base_reader = PdfReader(base_pdf)
        overlay_reader = PdfReader(overlay_pdf)
        writer = PdfWriter()
        overlay_page = overlay_reader.pages[0]
        for base_page in base_reader.pages:
            base_page.merge_page(overlay_page)
            writer.add_page(base_page)
        with open(output_pdf, "wb") as f:
            writer.write(f)
    except Exception as e:
        print(f"Error merging {base_pdf}: {e}")

TEMPLATE_FILES = [
    "Code Review Template.pdf",
    "Performance review template.pdf",
    "Post-Code Documentation Template.pdf",
    "Scope Document template.pdf",
    "Sprint Template.pdf",
]

if __name__ == "__main__":
    draw_grid_overlay("grid.pdf")
    for template in TEMPLATE_FILES:
        if not os.path.exists(template):
            print(f"Missing: {template}")
            continue
        output_name = template.replace(".pdf", "_with_grid.pdf")
        merge_overlay(template, "grid.pdf", output_name)
        print(f"Created: {output_name}")

