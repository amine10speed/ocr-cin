from fastapi import FastAPI, File, UploadFile
import shutil
from app.ocr import perform_ocr
import os

app = FastAPI()

@app.post("/ocr/")
async def ocr_endpoint(file: UploadFile = File(...), lang: str = "eng", is_arabic: bool = False):
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # Perform OCR
        extracted_text = perform_ocr(file_location, lang=lang, is_arabic=is_arabic)

        os.remove(file_location)  # Clean up the temporary file
        return {"message": "OCR completed successfully", "text": extracted_text}
    except Exception as e:
        os.remove(file_location)
        return {"message": "Error during OCR", "error": str(e)}
