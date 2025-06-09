from PIL import Image

from app.ocr import extract_text_from_image


def test_receipt_text():
    img = Image.open("tests/sample_receipt.jpg")  # Place test image here
    assert img is not None

    text = extract_text_from_image(img)
    assert "Total" in text or "Receipt" in text
