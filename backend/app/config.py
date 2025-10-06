from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
import os
from pathlib import Path

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# knowledge base directory
KB_DIR = Path(__file__).resolve().parent / "data" / "knowledge_base"
# vector store directory
VECTOR_STORE_DIR = Path(__file__).resolve().parent / "data" / "vector_store"

def get_chat_model():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        google_api_key=GOOGLE_API_KEY, 
        temperature=0.7
    )

    return llm
