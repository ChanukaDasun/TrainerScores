# setup weaviate vector database
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure, Property, DataType
from app.config import WEAVIATE_URL, WEAVIATE_KEY
from weaviate.classes.query import MetadataQuery

weaviate_url = WEAVIATE_URL
weaviate_key = WEAVIATE_KEY

client = weaviate.connect_to_weaviate_cloud(
    cluster_url= weaviate_url,
    auth_credentials=Auth.api_key(weaviate_key),
)

collection = client.collections.use("Rag_collection")

res = collection.query.hybrid(query="certificates", limit=5, alpha=0.3)

print(res)

print(client.collections.list_all().keys())

client.close()