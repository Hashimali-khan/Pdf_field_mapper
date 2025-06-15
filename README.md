🧾 PDF Field Mapper with Grid Overlay
This tool helps you visually map coordinates on PDF templates by overlaying a grid. It's useful for projects that need precise positioning of text, form fields, or annotations in automated PDF generation tasks.

📌 Features
Adds a grid overlay to your existing PDF templates

Coordinates are shown in PDF points (1 point = 1/72 inch)

Helps you determine exact positions for inserting dynamic content (like form fields)

📁 Project Structure
graphql
Copy code
pdf_field_mapper/
├── grid_overlay.py       # Main script
├── grid.pdf              # Auto-generated overlay file
├── [Template PDFs]       # Your input PDFs (see below)
├── [*_with_grid.pdf]     # Output PDFs with overlay
📥 Input PDFs
Make sure the following template files are placed in the project directory:

Code Review Template.pdf

Performance review template.pdf

Post-Code Documentation Template.pdf

Scope Document template.pdf

Sprint Template.pdf

If a file is missing, the script will notify you and skip that template.

⚙️ How It Works
Grid Generation
A grid of vertical and horizontal lines is drawn every 20 points (about 0.28 inches). Each line is labeled with its coordinate to help you locate positions visually.

PDF Merge
The grid is then merged on top of each page of your template PDFs.

Output Files
Output files will have the same name as the original but with _with_grid.pdf suffix, e.g.
Scope Document template_with_grid.pdf

🚀 How to Run
1. Set up the environment
bash
Copy code
python -m venv venv
venv\Scripts\activate  # On Windows
pip install PyPDF2 reportlab
2. Run the script
bash
Copy code
python grid_overlay.py
📐 Coordinate System Notes
All coordinates are in points (1 pt = 1/72 inch)

Origin (0, 0) is at the bottom-left corner of the page

Grid spacing: 20 pts

Useful for PDF editing libraries like ReportLab, PyMuPDF, or PyPDF2

📸 Example Output
You’ll get files like:

Scope Document template_with_grid.pdf

Sprint Template_with_grid.pdf

Open them in a PDF viewer — you’ll see the labeled grid overlay to help you decide where to place content.

🛠 Built With
PyPDF2 – For reading and merging PDFs

ReportLab – For generating the grid overlay

💡 Use Case Ideas
Designing fillable PDF forms

Mapping form field coordinates for autofill

UI/UX field alignment for generated reports

Annotating field templates for internal documentation

