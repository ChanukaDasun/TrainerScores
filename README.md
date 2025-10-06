# 🧠 TrainerScores

TrainerScores is a **Retrieval-Augmented Generation (RAG)** application built with **FastAPI** (backend) and **React + TypeScript** (frontend).  
It enables users to upload documents, store their embeddings, and query them via an intelligent chat interface powered by vector search and LLMs.

---

## 🚀 Tech Stack

### Backend
- **FastAPI** — REST API framework  
- **LangChain** — RAG pipeline orchestration  
- **ChromaDB** — Local vector store for embeddings  
- **OpenAI / Hugging Face Models** — Embedding & generation  
- **Pydantic** — Schema validation  
- **Uvicorn** — ASGI server  

### Frontend
- **React (TypeScript)** — Component-based UI  
- **Vite** — Build tool  
- **Axios** — API communication  

### Infrastructure
- **Docker** — Containerized services  
- **Kubernetes / Docker Compose** — Deployment options  

---

## 🏗️ Project Structure

TrainerScores/
├─ backend/
│ ├─ app/
│ │ ├─ main.py # FastAPI entry
│ │ ├─ config.py # env vars, model paths, settings
│ │ ├─ api/
│ │ │ ├─ v1/
│ │ │ │ ├─ upload.py # file upload & ingestion endpoints
│ │ │ │ ├─ query.py # chat/query endpoints
│ │ │ │ └─ admin.py # admin utilities
│ │ ├─ services/
│ │ │ ├─ ingestion.py # file parsing, chunking, metadata extraction
│ │ │ ├─ embeddings.py # embedding model wrapper
│ │ │ ├─ vectorstore.py # create/load/search vector store
│ │ │ ├─ rag_chain.py # LangChain RAG pipeline
│ │ │ └─ utils.py # shared utilities
│ │ ├─ models/ # Pydantic request/response schemas
│ │ ├─ workers/ # background task workers (optional)
│ │ └─ persistence/
│ │ └─ chroma_data/ # persisted vector store
│ ├─ requirements.txt # backend dependencies
│ └─ Dockerfile # backend container setup
│
├─ frontend/
│ ├─ src/
│ │ ├─ components/ # ChatWindow, UploadForm, etc.
│ │ ├─ api/ # backend API call definitions
│ │ └─ App.tsx # main React component
│ └─ package.json # frontend dependencies & scripts
│
├─ infra/
│ ├─ k8s/ # Kubernetes manifests
│ └─ docker-compose.yml # local multi-container setup
│
└─ README.md # this file