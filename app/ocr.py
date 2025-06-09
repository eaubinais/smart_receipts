import pytesseract
from PIL import Image


def extract_text_from_image(image: Image.Image) -> str:
    """Perform OCR on a PIL image."""
    text = pytesseract.image_to_string(image)
    return text.strip()
