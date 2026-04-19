import chromadb
from chromadb import Settings
from sentence_transformers import SentenceTransformer

#initializing embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

#load persistent vector store
client = chromadb.PersistentClient(path="vector_store")

collection = client.get_collection(name="schema_index")

def retrieve_relevant_schema(question, k=5):

    #embed the question
    question_embedding = model.encode(question).tolist()

    #query vector database
    results = collection.query(
        query_embeddings=[question_embedding],
         n_results = k
    )

    #extract shcema chunks
    schema_chunks = results["documents"][0]

    return schema_chunks