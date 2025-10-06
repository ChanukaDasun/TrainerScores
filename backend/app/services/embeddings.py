from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from PIL import Image
import pytesseract
from app.config import KB_DIR, VECTOR_STORE_DIR
from app.services.preprocess import preprocess_image as preprocess
from app.config import get_chat_model

image_paths = [
    KB_DIR / "1628163810175.jpeg", 
    KB_DIR / "1685694796403.jpeg", 
    KB_DIR / "1ffce456bac17e99460c1070d7248883.jpg",
    KB_DIR / "35fb34625a5c58f45262593238a0b9e5.jpg", 
    KB_DIR / "Certification-Certificate.jpg", 
    KB_DIR / "Duminda-PT-Kuwait-Training-Certificate-6.webp",
    KB_DIR / "EEOmgLrU4AENw_H.jpg", 
    KB_DIR / "ISSA_Digital_Certificate.webp", 
    KB_DIR / "Screenshot-2025-01-27-at-3.20.15 PM.png",
    KB_DIR / "b26740c45c568bfccd3c5ebe94916f29.jpg", 
    KB_DIR / "cad1ef5c097c49d4dad04e10edabeaca.jpg", 
    KB_DIR / "certificado-cross-training-2.jpg",
    KB_DIR / "certified-international-personal-trainer-certificate.jpg", 
    KB_DIR / "f5f8488d9fc1cb03c28d536450595809.jpg",
    KB_DIR / "ipt-.jpg"
]

def generate_documents_from_images(image_paths):
  documents = []
  print(f"🔄️ Extracting and preprocessed documents from images....")
  for img_path in image_paths:
    # first extract info from images using OCR
    img = Image.open(img_path)
    text = pytesseract.image_to_string(img)

    # preprocess each image info
    llm = get_chat_model()
    context = preprocess(text, llm)
    print(f"Extracted and preprocessed document: {context}")
    documents.append(context)

  print(f"✅ Extracted and preprocessed {len(documents)} documents from images.")
  return documents

def convert_doc_to_text(documents):
  text_list = []
  for doc in documents:
    text = f"""
      Certificate Title: {doc['certificate_title']}, Recipient Name: {doc['recipient_name']}, Institution: {doc['institution_name']}, Certificate ID: {doc['certificate_id']}, Issue Date: {doc['issue_date'] or 'Not specified'}Other Details: {doc['other_details']}
    """
    text_list.append(text)
  return text_list


def chunk_text(text):
  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0,
    separators=["\n\n", "\n", ".", " ", ""]
  )
  text_context = "\n\n".join(str(p) for p in text)
  text_chunks = text_splitter.split_text(text_context)

  return text_chunks


def embed_and_save(text_chunks):
    # Initialize embeddings model
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Create the Chroma database from text chunks
    db = Chroma.from_texts(
        texts=text_chunks,
        embedding=embeddings,
        persist_directory=str(VECTOR_STORE_DIR)
    )

    # Save to disk
    db.persist()
    print(f"✅ Vector store created and saved at: {VECTOR_STORE_DIR}")
    return db

def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = Chroma(
        persist_directory=str(VECTOR_STORE_DIR),
        embedding_function=embeddings
    )
    print("📂 Vector store loaded successfully")
    return db

# main execution
def embeddings_main():
    documents = generate_documents_from_images(image_paths)
    text = convert_doc_to_text(documents)
    text_chunks = chunk_text(text)

    db = embed_and_save(text_chunks)

if __name__ == "__main__": 
  embeddings_main()