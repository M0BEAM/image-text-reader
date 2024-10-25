from PIL import Image
import pytesseract

# For Windows users: Add the path to the tesseract.exe if it's not added to PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image from file
image_path = "./image.png"  # Replace with your image path
img = Image.open(image_path)

# Perform OCR on the image
text = pytesseract.image_to_string(img)

# Print the extracted text
print("Extracted Text: ")
print(text)
