from fastapi import APIRouter, HTTPException
from io import BytesIO
import requests
from PIL import Image
import pytesseract
from app.models.certificate_schema import ReadCertificateRequest, CertificateResponse
from app.services.preprocess import preprocess_image
from app.config import get_chat_model

router = APIRouter()

# Set the tesseract executable path manually
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

llm = get_chat_model()

@router.post("/read")
def read_certificate(certificate: ReadCertificateRequest) -> CertificateResponse:
    if not certificate.certificate_path:
        raise HTTPException(status_code=400, detail="Certificate path is required")
    try:
        response = requests.get(certificate.certificate_path)
        response.raise_for_status()  # raise if download fails
        image = Image.open(BytesIO(response.content))
        text = pytesseract.image_to_string(image)

        json_data = preprocess_image(text, llm)
        print("Preprocessed JSON Data:", json_data)  # Debugging line to check the

        return CertificateResponse(certificate_text=text)
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Error fetching image from URL: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

