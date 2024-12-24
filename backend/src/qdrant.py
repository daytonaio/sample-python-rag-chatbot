from langchain_community.vectorstores import Qdrant
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader

from langchain_huggingface import HuggingFaceEmbeddings
from qdrant_client import QdrantClient, models
from langchain_qdrant import QdrantVectorStore
from decouple import config

qdrant_api_key = config('QDRANT_API_KEY')
qdrant_url = config("QDRANT_URL")
collection_name= 'naya'


client = QdrantClient(
    url=qdrant_url,
    api_key=qdrant_api_key
)
embeddings_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
embeddings_docs= embeddings_model.embed_documents([
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
    ])
embeddings_size= len(embeddings_docs[0])
text_splitter= RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20, length_function=len)


def create_collection(collection_name):
    existing_collections = [collection.name for collection in client.get_collections().collections]
    
    if collection_name in existing_collections:
        print(f"Collection '{collection_name}' already exists.")
    else:
        print(f"Creating collection '{collection_name}'.")
        client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE)  # Adjust size if needed
        )
    print(f'collection {collection_name} create successfully of size {embeddings_size}')

vector_store =QdrantVectorStore(client=client,collection_name=collection_name,embedding=embeddings_model)
def upload_website_to_collection(url:str):
    loader= WebBaseLoader(web_path=url)


    return f'successfully uploaded {len(docs)} documents to collection {collection_name}'

create_collection(collection_name)
upload_website_to_collection('https://hamel.dev/blog/posts/evals')

#upto 15 minutes