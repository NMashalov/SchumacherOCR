# Load model directly
import pytesseract
from PIL import Image

class Tesseract:
    '''
    Suitable for workbooks
    '''
    def __init__(self, img_folder):
        pass

    def ocr(self):
        print(pytesseract.image_to_string(Image.open('test.png')))