from app.services.embeddings import generate_documents_from_images, convert_doc_to_text
from app.services.weaviate_vectorstore import weaviate_client
from weaviate.classes.query import MetadataQuery

def get_relevance_score(json_data, llm):
  # load vector store
  client = weaviate_client()
  collection = client.collections.use("Rag_collection")

  query = convert_doc_to_text([json_data])

  query = " ".join(query)
  print(f"query for vector store: {query}")

  # retrive relevent chunks
  context_for_new_doc = collection.query.hybrid(query=query, limit=10, alpha=0.3)
  print(f"similar context for inputed image: {context_for_new_doc}")
  input_doc_text = " ".join([obj.properties["content"] for obj in context_for_new_doc.objects])

  context = input_doc_text

  print(f"context for llm: {context}")

  # define the prompt template
  query_template = f"""
  You are a validator of personal trainer certificates. Don't use your own general knowledge about Personal Trainer certificates
  and generate answers using related documents for each answer! These Related documents all are extacted from personal trainer certificates.
  Then You have found some repeted words from like institution name identify them as valid sources for a personal trainer.
  You are given certificate details retrieved from a database.

  Related documents:
  {context}

  Your task is to evaluate below certificate whether the certificate is about a "Personal Trainer" certification.
  given document: (this document is in Json format)
  {json_data}

  Instructions:
  1. Analyze the retrieved certificate details carefully.
  2. Use both the retrieved information and your own general knowledge about Personal Trainer certificates.
  3. Decide how strongly this certificate is related to a Personal Trainer certificate.
  4. Provide your reasoning clearly.
  5. Finally, give a relevance score between 1 and 10:
    - 1 = Not related at all
    - 5 = Partially related / has some overlap
    - 10 = Directly and strongly related to a Personal Trainer certificate

  Answer format:
  Reasoning: <your explanation>
  Score: <number between 1 and 10>
  """
  answer = llm.invoke(query_template)
  client.close()
  return answer