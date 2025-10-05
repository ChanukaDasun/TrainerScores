from fastapi import APIRouter
from app.api.routes import test

router = APIRouter()

# this is the route for the test endpoint
router.include_router(test.router, prefix="/test", tags=["test"])