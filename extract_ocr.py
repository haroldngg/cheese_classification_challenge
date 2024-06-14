import easyocr
from PIL import Image
reader = easyocr.Reader(['en'])

def easyocr_from_path(image_path):
    text = reader.readtext(image_path)
    return text


def easyocr_from_array(array):
    pil_image = Image.fromarray(array)
    text = reader.readtext(pil_image)
    return text
