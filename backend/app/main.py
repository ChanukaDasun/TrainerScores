from fastapi import FastAPI, HTTPException # raise HTTPException(status_code=400, detail="Bad Request")
from app.api import router as api_router
from app.config import get_chat_model

app = FastAPI()

# initialize the chat model
llm = get_chat_model()

@app.get("/")
def root():
    return {"message": "Hello, World!"}


app.include_router(api_router, prefix="/api")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)