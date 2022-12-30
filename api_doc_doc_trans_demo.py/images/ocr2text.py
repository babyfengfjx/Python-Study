import pytesseract
image = 'output_0.jpg'
text = pytesseract.image_to_string(image)
print(text)