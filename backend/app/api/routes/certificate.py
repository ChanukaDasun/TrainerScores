from fastapi import APIRouter, HTTPException
from io import BytesIO
import requests
from PIL import Image
import pytesseract
from app.models.certificate_schema import ReadCertificateRequest, CertificateResponse, CertificateScoreResponse
from app.services.preprocess import preprocess_image
from app.services.scoring import get_relevance_score
from app.config import get_chat_model
import re

router = APIRouter()

# Set the tesseract executable path manually
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" # update this path as per your installation



@router.post("/read")
def read_certificate(certificate: ReadCertificateRequest) -> CertificateResponse:
    if not certificate.certificate_path:
        raise HTTPException(status_code=400, detail="Certificate path is required")
    try:
        response = requests.get(certificate.certificate_path)
        response.raise_for_status()  # raise if download fails
        image = Image.open(BytesIO(response.content))
        text = pytesseract.image_to_string(image)
        llm = get_chat_model()
        json_data = preprocess_image(text, llm)
        print("Preprocessed JSON Data:", json_data)  # Debugging line to check the

        return CertificateResponse(certificate_text=text)
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Error fetching image from URL: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/score")
def generate_score(certificate: ReadCertificateRequest) -> CertificateScoreResponse:
    if not certificate.certificate_path:
        raise HTTPException(status_code=400, detail="Certificate path is required")

    try:
        response = requests.get(certificate.certificate_path)
        response.raise_for_status()  # raise if download fails
        image = Image.open(BytesIO(response.content))
        text = pytesseract.image_to_string(image)
        print(f"Extracted text from image: {text}")  # Debugging line to check OCR output

        llm = get_chat_model()        
        json_data = preprocess_image(text, llm) # preprocessed data from certificate
        print(f"preprocessed json data: {json_data}")

        image_score = get_relevance_score(json_data, llm)
        print(f"Generated score: {image_score}")

        # pharse the score and reasoning from the llm response
        raw_text = image_score.content.strip() if hasattr(image_score, "content") else str(image_score)
        print(f"Raw LLM response: {raw_text}")

        # Step 5: Parse Reasoning and Score
        reasoning_match = re.search(r"Reasoning:\s*(.+?)(?:\n|$)", raw_text, re.DOTALL)
        score_match = re.search(r"Score:\s*([\d.]+)", raw_text)

        reasoning = reasoning_match.group(1).strip() if reasoning_match else "No reasoning found."
        score = float(score_match.group(1)) if score_match else 0.0

        return CertificateScoreResponse(reasoning=reasoning, score=score)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))