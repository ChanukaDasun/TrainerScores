from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def get_chat_model():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-pro", 
        google_api_key=GOOGLE_API_KEY, 
        temperature=0.7
    )

    return llm
