import os
from fpdf import FPDF

def generate_pdf(username, image_type, disease, confidence):

    os.makedirs("reports", exist_ok=True)

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=14)

    pdf.cell(200, 10, txt="AI Disease Report", ln=True)
    pdf.cell(200, 10, txt=f"Patient: {username}", ln=True)
    pdf.cell(200, 10, txt=f"Image Type: {image_type}", ln=True)
    pdf.cell(200, 10, txt=f"Disease: {disease}", ln=True)
    pdf.cell(200, 10, txt=f"Confidence: {confidence:.2f}%", ln=True)

    path = f"reports/{username}.pdf"

    pdf.output(path)

    return path