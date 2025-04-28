# ML_Vertical_app

# import easyocr, re

Imported easyocr for OCR (text extraction from images) and re for regular expressions (to extract specific fields from text).

# def extract_text_from_image(image_path: str) -> str:

This function takes image path as input and uses EasyOCR to extract all the visible text.

reader = easyocr.Reader(['en']): Create a new OCR reader that reads english text. 

result = reader.readtext(image_path, detail = 0): Extract all text lines as simple strings (without bounding box details)

" ".join(result) : Join all text lines into one long string to make searching easier

# def extract_fields(ocr_text: str) -> dict:

This function searches inside the OCR text for important fields like Name, Address and DOB.

fields = { "Name": None, "Address": None, "DOB": None }: Initialize a dictionary to store extracted fields

name_match = re.search(r'Name[:\s]*([A-Za-z\s]+)', ocr_text): Use regex to find where Name is mentioned and capture the text after it.

# def validate_document(fields: dict) -> bool:

Checks if Name, DOB are actually found or not.

If both fields are non-empty, it returns True (document is valid) or else False

# def process_document(image_path: str) -> dict:

Main pipeline function.

It calls OCR, then field extraction, then validation and finally returns a result dictionary.

#if __name__ == "__main__"": 

Main program block to test the code by manually giving an image path
