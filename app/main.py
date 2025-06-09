import io

from fastapi import FastAPI, File, UploadFile
from PIL import Image

from app.ocr import extract_text_from_image

app = FastAPI()

@app.post("/ocr")
async def ocr_endpoint(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    text = extract_text_from_image(image)
    return {"text": text}
