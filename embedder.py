import cohere
import os

from dotenv import load_dotenv
load_dotenv()


co = cohere.Client(os.getenv("COHERE_API_KEY"))

def embed_text(texts: list[str]) -> list[list[float]]:
    """
    Metinleri embed formatına dönüştürür.
    """
    response = co.embed(
        texts=texts,
        model="embed-english-v3.0",
        input_type="search_document"
    )
    return response.embeddings
