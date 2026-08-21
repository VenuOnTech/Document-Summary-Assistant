import pdfplumber
import pytesseract
from PIL import Image
import io

def extract_text_from_pdf(file_bytes):
    """Extracts text from a PDF while preserving basic structure."""
    text = ""
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n\n"
    return text.strip()

def extract_text_from_image(file_bytes):
    """Extracts text from scanned images using Tesseract OCR."""
    image = Image.open(io.BytesIO(file_bytes))
    # pytesseract acts as a wrapper for the system-level Tesseract engine
    text = pytesseract.image_to_string(image)
    return text.strip()
