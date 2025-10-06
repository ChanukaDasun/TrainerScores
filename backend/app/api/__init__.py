from fastapi import APIRouter
from app.api.routes import test, chat, certificate

router = APIRouter()

router.include_router(test.router, prefix="/test", tags=["test"]) # this is the route for the test endpoint
router.include_router(chat.router, prefix="/chat", tags=["chat"])
router.include_router(certificate.router, prefix="/certificate", tags=["certificate"])