import pytesseract
from PIL import Image
from chat_detector import detect_scam_message

def analyze_screenshot(path):

    img=Image.open(path)

    text=pytesseract.image_to_string(img)

    risk=detect_scam_message(text)

    return {
    "text":text,
    "risk":risk
    }