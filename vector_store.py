import chromadb
from chromadb.config import Settings
from embedder import embed_text

import chromadb

chroma_client = chromadb.PersistentClient(path="db/chroma_store")


collection = chroma_client.get_or_create_collection(name="cv_database")

def add_cv_to_vector_store(doc_id: str, text: str):
    embedding = embed_text([text])[0]
    collection.add(documents=[text], embeddings=[embedding], ids=[doc_id])

def retrieve_similar_cvs(query: str, top_k=3):
    embedding = embed_text([query])[0]
    results = collection.query(query_embeddings=[embedding], n_results=top_k)
    return results['documents'][0]
