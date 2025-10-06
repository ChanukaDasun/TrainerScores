import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure, Property, DataType
from app.config import WEAVIATE_URL, WEAVIATE_KEY

def weaviate_client():

    client = weaviate.connect_to_weaviate_cloud(
        cluster_url= WEAVIATE_URL,
        auth_credentials=Auth.api_key(WEAVIATE_KEY),
    )

    existing_collections = client.collections.list_all().keys()

    print(existing_collections)

    if "Rag_collection" not in existing_collections:
        client.collections.create(
            "Rag_collection",
            properties=[
                Property(name="content", data_type=DataType.TEXT),
            ],
            vector_config=[
                Configure.Vectors.text2vec_weaviate(
                    name="title_vector",
                    model="Snowflake/snowflake-arctic-embed-l-v2.0",
                )
            ],
        )
    
    return client

