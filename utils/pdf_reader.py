from langchain.document_loaders import PyPDFLoader
from tempfile import NamedTemporaryFile

def extract_text_from_pdf(uploaded_file) -> str:
    """
    Streamlit'ten gelen PDF dosyasını geçici dosyaya yazıp metnini döndürür.
    """
    with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file.flush()

        loader = PyPDFLoader(tmp_file.name)
        pages = loader.load()

        # Sayfalardaki metinleri birleştir
        full_text = "\n\n".join([page.page_content for page in pages])
        return full_text
