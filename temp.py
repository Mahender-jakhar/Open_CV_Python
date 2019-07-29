import pytesseract
import cv2 as cv
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Mahender jakhar\Desktop\OPEN_CV_EX\venv\Lib\site-packages\pytesseract"
img = Image.open('open.png')

result = pytesseract.image_to_string(img)

with open('te.txt',mode='w') as file:
    file.write(result)



