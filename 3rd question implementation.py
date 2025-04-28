import easyocr
import re

#OCR Extraction function
def extract_text_from_image(image_path: str) -> str:
    #Runs OCR on the input image sand returns the extracted text

    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path, detail=0)
    full_text = " ".join(result)
    return full_text

#Field Extraction function
def extract_fields(ocr_text: str) -> dict:
    #Parses OCR text and tries to extract important fields like Name, ID, DOB. Returns a dictionary of fields.

    fields = {
        "Name": None,
        "ID": None,
        "DOB": None
    }

    #Try to find Name 
    name_match = re.search(r'Name[:\s]*([A-Za-z\s]+)', ocr_text)
    if name_match:
        fields["Name"] = name_match.group(1).strip()

    #Try to find DOB (common date formats)
    dob_match = re.search(r'(\d{2}[/-]\d{2}[/-]\d{4})', ocr_text)
    if dob_match:
        fields["DOB"] = dob_match.group(1).strip()

    return fields

#Document validation function
def validate_document(fields: dict) -> bool:
    #checks if essential fields like Name and DOB are present

    if fields["Name"] and fields["ID"]:
        return True
    return False

#Main function
def process_document(image_path: str) -> dict:
    
    ocr_text = extract_text_from_image(image_path)
    fields = extract_fields(ocr_text)
    is_valid = validate_document(fields)

    return {
        "fields": fields,
        "is_valid": is_valid
    }

#Example usage
if __name__ == "__main__":
    image_path = "sample_id_card.jpg"
    result = process_document(image_path)
    print("Extracted Fields:", result["fields"])
    print("Is Valid Document:", result["is_valid"])