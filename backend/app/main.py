from fastapi import FastAPI, HTTPException # raise HTTPException(status_code=400, detail="Bad Request")
from app.api import router as api_router
from app.config import get_chat_model, VECTOR_STORE_DIR
from app.services.embeddings import load_vectorstore
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend origins
app.add_middleware(
    CORSMiddleware
)

# initialize the chat model
llm = get_chat_model()

@app.get("/")
def root():
    return {"message": "Hello, World!"}

# handle startup event to load vector store
@app.on_event("startup")
def startup_event():
    print("🚀 Starting up the application...")
    try:
        print(f"🔗 Loading vector store from: {VECTOR_STORE_DIR}")
        app.state.db = load_vectorstore()
        print("✅ Vector store loaded and ready.")
    except Exception as e:
        print(f"❌ Error loading vector store: {e}")
        raise HTTPException(status_code=500, detail="Failed to load vector store")
    

app.include_router(api_router, prefix="/api")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)