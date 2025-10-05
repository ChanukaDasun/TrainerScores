File structure:

TrainerScores/
├─ backend/
│  ├─ app/
│  │  ├─ main.py                 # FastAPI entry
│  │  ├─ config.py               # env vars, model selection, paths
│  │  ├─ api/
│  │  │  ├─ v1/
│  │  │  │  ├─ upload.py         # upload & ingestion endpoints
│  │  │  │  ├─ query.py          # chat/query endpoints
│  │  │  │  └─ admin.py
│  │  ├─ services/
│  │  │  ├─ ingestion.py         # file parsing, chunking, metadata extraction
│  │  │  ├─ embeddings.py        # wraps embedding model(s)
│  │  │  ├─ vectorstore.py       # create/load/search vector store
│  │  │  ├─ rag_chain.py         # LangChain chain setup
│  │  │  └─ utils.py
│  │  ├─ models/                 # pydantic request/response schemas
│  │  ├─ workers/                # background task workers (optional)
│  │  └─ persistence/
│  │     └─ chroma_data/         # persisted vector store (persist_directory)
│  ├─ requirements.txt
│  └─ Dockerfile
├─ frontend/
│  ├─ src/
│  │  ├─ components/             # ChatWindow, UploadForm
│  │  ├─ api/                    # calls to backend
│  │  └─ App.tsx
│  └─ package.json
├─ infra/
│  └─ k8s/ / docker-compose.yml
└─ README.md
