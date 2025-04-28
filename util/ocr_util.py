import pytesseract
from pdf2image import convert_from_path
import os

class UtilOCR:
    @staticmethod
    def extract_text(pdf_file: str, custom_type: str = None) -> str:
        """
        Extract text from a PDF file using OCR.
        
        Args:
            pdf_file (str): Path to the PDF file
            custom_type (str): Custom processing type for specific document formats
            
        Returns:
            str: Extracted text from the PDF
        """
        try:
            if not os.path.exists(pdf_file):
                raise FileNotFoundError(f"PDF file not found: {pdf_file}")
                
            # Convert PDF to images
            images = convert_from_path(pdf_file)
            
            # Extract text from each page
            extracted_text = []
            for i, image in enumerate(images):
                # Apply custom processing based on type if specified
                if custom_type:
                    # Add custom preprocessing logic here based on custom_type
                    pass
                
                # Perform OCR
                text = pytesseract.image_to_string(image)
                extracted_text.append(text)
            
            return "\n".join(extracted_text)
            
        except Exception as e:
            print(f"Error extracting text from PDF: {e}")
            return ""









