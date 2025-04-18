from cohere_chain import analyze_resume_rag
from vector_store import add_cv_to_vector_store
import os

def load_resume(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == "__main__":
    resume_text = load_resume("example_cv.txt")
    
    # Veritabanına ekleme (eğer yeni bir CV ise)
    add_cv_to_vector_store("example_1", resume_text)

    job_title = input("Pozisyon gir (örneğin: Backend Developer): ")
    print("\n--- ANALİZ ---\n")
    print(analyze_resume_rag(resume_text, job_title))
