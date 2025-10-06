# 🧠 TrainerScores

TrainerScores is a **Retrieval-Augmented Generation (RAG)** application built with **FastAPI** (backend) and **React + AntDesign** (frontend).  
It enables users to upload documents, store their embeddings, and query them via an intelligent chat interface powered by vector search and LLMs.

---

## 🚀 Tech Stack

### Backend
- **FastAPI** — REST API framework  
- **LangChain** — RAG pipeline orchestration  
- **Weaviate cloud** — Local vector store for embeddings  
- **Snowflake/snowflake-arctic-embed-l-v2.0** — Embeddings
- **gemini-2.5-pro** — Generation  
- **Pydantic** — Schema validation  
- **Uvicorn** — ASGI server  

### Frontend
- **React with AntDesign** — Component-based UI  
- **Vite** — Build tool  
- **Axios** — API communication  

---

## 🏗️ Project Structure

```
TrainerScores/
│
├── backend/
│   ├── app/
│   │   ├── main.py                          # FastAPI entry
│   │   ├── config.py                        # env vars, model paths, settings
│   │   │
│   │   ├── api/
|   |   |   ├── __init__.py
│   │   │   └── routes
│   │   │       ├── certificate.py           # read and generate scores from certificates
│   │   │       ├── chat.py                  # chat endpoint
│   │   │       └── test.py                  # testing purpose
│   │   │
│   │   ├── services/
│   │   │   ├── preprocess.py                # extract text from certificates (OCR) and convert it into json using llm
│   │   │   ├── embeddings.py                # embedding model wrapper
│   │   │   ├── scoring.py                   # generate score based on extracted certificate data
│   │   │   └── weaviate_vectorstore.py      # define weaviate vector store 
│   │   │
│   │   ├── models/                          # Pydantic request/response schemas
|   |   |   ├── certificate_schema.py           
│   │   │   └── chat_schema.py
|   |   |
│   │   ├── test/                            # all the test files are here
│   │   └── data/
│   │       └── knowledge_base/              # all the preloaded personal trainer certificates
│   │
│   └──  requirements.txt                    # backend dependencies
│   |
│   └──  .env                                # .env file gose here
│  
│
├── frontend/
│   ├── src/
│   │   ├── assets/                          # ChatWindow, UploadForm, etc.
│   │   ├── utils/                           # backend API call definitions
│   │   └── App.jsx                          # main React component
│   │
│   └── package.json                         # frontend dependencies & scripts
│
│
└── README.md                                # this file
```

---

## 📦 Installation

### Prerequisites
- Python 3.9+
- Node.js 16+

---

## 🔧 Configuration

Create a `.env` file in the `backend/` directory:

```env
WEAVIATE_URL=your_weaviate_cloud_url
WEAVIATE_API_KEY=your_api_key
GEMINI_API_KEY=your_gemini_api_key
```
also install tesseract-ocr-w64-setup-5.5.0.20241111 and set its path as environment variable. also add this path (tesseract executable path) into the {app > api > routes > certificate.py} (I mentioned it clearly in this file)! 

---

### Backend Setup
```bash
cd backend
python -m venv myenv (to create python virtual environment for first time -> to activate it "myenv\Scripts\activate" : to deactivate it "deactivate")
pip install -r requirements.txt
python -m app.services.embeddings (run this command only when you use this app for the first time)
uvicorn app.main:app --reload (strat fast api backend)
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

---

## 🚀 Usage

1. **Upload Documents**: Use the frontend interface to upload trainer certificates 
2. **Get AI Responses**: The RAG system retrieves relevant context and generates certificate score along with the reason  

---
