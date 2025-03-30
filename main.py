Creating a complete "smart-invoice" system is quite an extensive task, but I will provide you with a basic version of an automated invoice generation and management system using OCR (Optical Character Recognition) in Python. This program will involve reading invoices using OCR, extracting relevant information, and generating a structured invoice.

To work with OCR in Python, we can use the `pytesseract` library along with `Pillow` for image processing. Please note that this project is just a starting point and can be expanded significantly with additional features such as database integration, web interfaces, etc.

### Prerequisites:
1. Install Tesseract OCR on your system. You can download it from [here](https://github.com/tesseract-ocr/tesseract).
2. Set up the `pytesseract` and `Pillow` libraries.
   ```bash
   pip install pytesseract pillow
   ```

### Python Program

Here's a basic implementation:

```python
import pytesseract
from PIL import Image
import re
import os

# Configure pytesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update the path if required

def read_image_text(image_path):
    """Extract text from an image using OCR."""
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"Error reading image {image_path}: {e}")
        return None

def parse_invoice(text):
    """Parse essential invoice details from extracted text."""
    
    try:
        invoice_data = {}

        # Simple regex patterns to extract information
        invoice_number_pattern = r"Invoice Number:\s*(\d+)"
        date_pattern = r"Date:\s*([\d-]+)"
        amount_pattern = r"Total Amount:\s*\$?([\d,.]+)"

        invoice_data['invoice_number'] = re.search(invoice_number_pattern, text).group(1)
        invoice_data['date'] = re.search(date_pattern, text).group(1)
        invoice_data['total_amount'] = re.search(amount_pattern, text).group(1)

        return invoice_data
    except Exception as e:
        print(f"Error parsing invoice text: {e}")
        return None

def generate_invoice_report(invoice_data, output_path='invoice_report.txt'):
    """Generate a simple report from the extracted invoice data."""
    try:
        with open(output_path, 'w') as file:
            file.write("Invoice Report\n")
            file.write("====================\n")
            for key, value in invoice_data.items():
                file.write(f"{key.replace('_', ' ').title()}: {value}\n")
        print(f"Invoice report generated: {output_path}")
    except Exception as e:
        print(f"Error generating invoice report: {e}")

def process_invoice(image_path):
    """Process an invoice given its image path."""
    text = read_image_text(image_path)
    if text:
        invoice_data = parse_invoice(text)
        if invoice_data:
            generate_invoice_report(invoice_data)

# Example usage:
if __name__ == '__main__':
    image_file_path = 'path/to/your/invoice/image.png'  # Replace with your invoice image path
    if os.path.exists(image_file_path):
        process_invoice(image_file_path)
    else:
        print("Image file does not exist.")

```

### Program Overview
- **OCR Extraction**: The function `read_image_text()` opens an image file and extracts text using Tesseract OCR.
- **Parsing Text**: The function `parse_invoice()` uses regular expressions to extract key details such as "Invoice Number", "Date", and "Total Amount" from the text.
- **Report Generation**: The function `generate_invoice_report()` writes the extracted details into a report file.
- **Error Handling**: The program includes basic error handling to ensure smooth execution and notify users of issues encountered during image reading or processing.

### Next Steps
1. **Enhance Parsing**: Expand the regex patterns to include other relevant invoice details like vendor name, line items, etc.
2. **Database Integration**: Store extracted data in a database for easier access and management.
3. **GUI Development**: Utilize libraries like Tkinter or create a web interface with Flask/Django for user-friendly interaction.
4. **Multi-language Support**: Modify the OCR engine settings to accommodate invoices in various languages.