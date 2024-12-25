import pytesseract
from bidi.algorithm import get_display
import arabic_reshaper
import cv2

def perform_ocr(image_path, lang="eng", is_arabic=False):
    """
    Perform OCR on an image.

    :param image_path: Path to the input image.
    :param lang: Language for OCR (default: English).
    :param is_arabic: Whether the text is in Arabic for reshaping and reordering.
    :return: Extracted text.
    """
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Could not read image: {image_path}")

    # Convert to grayscale if needed
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform OCR
    text = pytesseract.image_to_string(gray, lang=lang).strip()

    # Handle Arabic text
    if is_arabic and text:
        text = get_display(arabic_reshaper.reshape(text))

    return text
