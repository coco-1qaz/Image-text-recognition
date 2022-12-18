import cv2
import pytesseract

img = cv2.imread('file')

config = r'-l chi_sim+eng --psm 6'
text = pytesseract.image_to_string(img, config=config, lang='chi_sim')

print("Test is:",text)