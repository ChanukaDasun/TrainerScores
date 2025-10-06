from pydantic import BaseModel, Field
from typing import List, Optional

class ReadCertificateRequest(BaseModel):
    certificate_path: str

class CertificateResponse(BaseModel):
    certificate_text: str

class CertificateScoreResponse(BaseModel):
    reasoning: str
    score: float