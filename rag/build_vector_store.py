import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

from .schema_chunks import load_schema_chunks

def build_vector_store():

    #load schema chunks
    chunks = load_schema_chunks()

    #initialize embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    #initialize chroma client
    client = chromadb.PersistentClient(path="vector_store")

    collection = client.create_collection(
        name = "schema_index"
    )

    #create embeddings
    embeddings = model.encode(chunks).tolist()

    #store in vector database
    for i, chunk in enumerate(chunks):

        collection.add(
            documents=[chunk],
            embeddings = [embeddings[i]],
            ids = [str(i)]
        )

    print("Vector store created successfully!")

    return collection
    
if __name__ == "__main__":
    build_vector_store()
