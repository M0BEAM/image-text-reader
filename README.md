
# Image Text Reader

This is a simple Python application that extracts text from images using Tesseract-OCR. It uses the `pytesseract` library for Optical Character Recognition (OCR) and `Pillow` for image processing.

## Features

- Extracts text from an image using OCR.
- Supports various image formats (e.g., PNG, JPEG).
- Can be extended with image pre-processing to improve OCR accuracy.

## Prerequisites

1. **Python** (version 3.6 or higher)
2. **Tesseract-OCR** (installed and added to PATH)
3. **Python libraries**: `pytesseract`, `Pillow`

### Installing Tesseract-OCR

- **Windows**: Download the installer from [here](https://github.com/UB-Mannheim/tesseract/wiki).
- **Linux**: Install via package manager:
  ```bash
  sudo apt install tesseract-ocr
  ```
- **macOS**: Install using Homebrew:
  ```bash
  brew install tesseract
  ```

After installation, make sure Tesseract is added to your system's PATH.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/M0BEAM/cls.git
   ```
2. Navigate to the project directory:
   ```bash
   cd image-text-reader
   ```
3. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the script**:
   ```bash
   python test.py
   ```
2. The app will read text from the image specified in the script.

   Example image path:
   ```python
   img = Image.open("sample_image.png")
   ```

## Customization

- **Change the Image**: Replace `"sample_image.png"` in the script with the path to your image.
- **Image Preprocessing**: You can preprocess the image (e.g., convert to grayscale, apply thresholding) to improve OCR accuracy.

## Example

Here's an example of extracting text from an image:
```python
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = Image.open("sample_image.png")
text = pytesseract.image_to_string(img)
print(text)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
