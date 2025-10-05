from fastapi import FastAPI
from app.api import router as api_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, World!"}

app.include_router(api_router, prefix="/api")